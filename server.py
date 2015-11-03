#!/usr/bin/python
#
#+	Copyright (c) 2014, 2015 Rikard Lindstrom <ornotermes@gmail.com>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import ConfigParser
from flask import *
import threading
import os.path
import sys, os, time
import pickle
sys.path.append("effects/")
sys.path.append("device/")

config = ConfigParser.ConfigParser()
config.read("config.ini")

webApp = Flask(__name__)

effect_module = None
effect_thread = None

class form:
	source = ""
	def render(self):
		return self.source
	
	def get(self, var):
		return "data." + var
		
	def start(self):
		self.source += "<form class=\"form-horizontal\">"
	
	def finnish(self):
		self.source += "</form>"
	
	def slider(self, var, label, min, max, step, start):
		self.source += render_template("form/slider.html", var = var, label = label, min = min, max = max, step = step, start = start) + "\n"
	

if config.has_option("session", "secretkey"):
	webApp.secret_key = config.get("session", "secretkey")

ledStrip = ""

def isLogedIn():
	return ('login' in session)
	
def getEffectFileName(effect):
	fileName = "effects/" + effect + ".py"
	fileName = fileName.replace("'", "'\\''").replace("..", "\.\.")
	return fileName

@webApp.route("/favicon.ico")
def favicon():
	return redirect("/static/img/ws2812b-16.png")

@webApp.route("/")
def index():
	return  render_template("index.html", stripConfig = strip.config )
		
@webApp.route("/robots.txt")
def robots():
	return "User-agent: *\nDisallow: /"

@webApp.route("/effects/", methods=["GET", "POST"])
def effects():
	if request.method == "POST":
		if request.form['edit']:
			return redirect("/edit/" + request.form['edit'])
		
	effectFiles = [ f[:-3] for f in os.listdir("effects/") if (os.path.isfile(os.path.join("effects/",f)) & f.endswith(".py")) ]
	effectFiles = sorted(effectFiles)
	return render_template("effects.html", effects = effectFiles, logedin = isLogedIn())
	
@webApp.route("/running/")
def running():
	obj = {}
	global effect_module
	global effect_thread
	obj = {"running" : False}
	if effect_thread:
		if effect_thread.is_alive():
			obj["running"] = True
			obj["name"] = effect_module.name
			obj["form"] = False
			if hasattr(effect_module, "form"):
				obj["form"] = effect_module.form.render()

	return jsonify(obj)

@webApp.route("/config/get/")
def configGet():
	global effect_module
	global effect_thread
	if effect_thread.is_alive():
		return jsonify(effect_module.config)
	

@webApp.route("/config/set/")
@webApp.route("/config/set/<name>/<typeName>/<value>/")
def configSet(name = None, typeName = None, value = None):
	global effect_module
	global effect_thread
	if isLogedIn() & bool(effect_module) & bool(name):
		if typeName == "bool": effect_module.config[name] = bool(value)
		if typeName == "int": effect_module.config[name] = int(value)
		if typeName == "float": effect_module.config[name] = float(value)
		if typeName == "str": effect_module.config[name] = str(value)
		
		print name, value, effect_module.config, typeName, (typeName == u"float")
		return "OK"
	return "FAIL"
		

@webApp.route("/config/save/")
def configSave():
	global effect_module
	global effect_thread
	if isLogedIn() & bool(effect_module):
		cfg_file = open("effects/" + effect_module.name + ".pkl", "w")
		pickle.dump(effect_module.config, cfg_file)
		cfg_file.close();
		return "OK"
	return "FAIL"
	
@webApp.route("/config/delete/")
def configDelete():
	global effect_module
	global effect_thread
	if isLogedIn() & bool(effect_module):
		cfg_path = "effects/" + effect_module.name + ".pkl"
		if (os.path.isfile(cfg_path)): os.remove(cfg_path)
		run(effect_module.name)
		return "OK"
	return "FAIL"

@webApp.route("/schedule/")
def schedule():
	return render_template("schedule.html")

@webApp.route("/about/")
def about():
	return render_template("about.html")

@webApp.route("/login/", methods=["GET", "POST"])
def login():
	loginfail = False
	if request.method == "POST":
		if request.form["password"]:
			if config.has_option("session", "password"):
				password = config.get("session", "password")
			else:
				password = False
				
			if request.form["password"] == password:
				session['login'] = True
			else:
				loginfail = True
				
	return render_template("login.html", logedin = isLogedIn(), loginfail = loginfail)
@webApp.route("/login/status/")
def loginStatus():
	return str(int(isLogedIn()))

@webApp.route("/logout/")
def logout():
	session.pop('login', None)
	return redirect(url_for('index'))

@webApp.route("/edit/<effect>")
@webApp.route("/edit/<effect>/<action>/", methods=["GET", "POST"])
def edit(effect=None, action=None):
	if (action=="save") & isLogedIn():
		edit_file = open(getEffectFileName(effect), "w")
		edit_file.write(request.form["data"])
		edit_file.close()
		return "Saved"
	if (action=="delete") & isLogedIn():
		os.remove(getEffectFileName(effect))
		return redirect(url_for('index'))
	if (action=="load"):
		if (os.path.exists(getEffectFileName(effect))):
			edit_file = open(getEffectFileName(effect))
		else:
			edit_file = open("effect-skel.py")
		text =  edit_file.read()
		edit_file.close()
		return(text)
	if (action=="exist"):
		return str(int(os.path.exists(getEffectFileName(effect))))
		
	if effect:
		return render_template("edit.html", effect = escape(effect), logedin = isLogedIn())
		
@webApp.route("/run/<effect>")
def run( effect = None ):
	if (bool(effect) & isLogedIn()):
		stop()
		global effect_module
		global effect_thread
		effect_module = __import__(effect)
		effect_module.strip = strip
		effect_module.name = effect
		effect_module.time = time
		effect_module.stop = False
		effect_module.config = {}
		effect_module.form = form()
		if hasattr(effect_module, "init"): effect_module.init()
		
		cfg_path = "effects/" + effect + ".pkl"
		if (os.path.isfile(cfg_path)):
			cfg_file = open(cfg_path)
			effect_module.config.update( pickle.load(cfg_file) )
			cfg_file.close()
		
		print(hasattr(effect_module, "show"))
		if hasattr(effect_module, "show"):
			effect_module.show()
			print effect_module.form.source
		
		effect_thread = threading.Thread(target=effect_module.run)
		effect_thread.start()
	return ""
	

@webApp.route("/stop/")
def stop():
	if isLogedIn():
		global effect_module
		global effect_thread
	
		if effect_module:
			effect_module.stop = True
	
		if effect_thread:
			while effect_thread.is_alive():
				effect_thread.join(1.0)
		
	return ""

if __name__ == "__main__":
	
	if config.has_option("server", "host"):
		host = config.get("server", "host")
	else:
		host = "127.0.0.1"
	
	if config.has_option("server", "port"):
		port = config.getint("server", "port")
	else:
		port = 5000
		
	if config.has_option("server", "debug"):
		if config.get("server", "debug") == "true":
			debug = True
		else:
			debug = False
	else:
		debug = False
	
	if config.has_option("device", "type"):
		device = __import__(config.get("device", "type"))
		strip = device.strip()
		strip.config.update(config.items("device"))
		strip.init()
	
	webApp.run(host=host, port=port, debug=debug)
