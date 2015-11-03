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

from random import *

def show():
	form.start()
	form.slider("hue", "Hue", 0.0, 1.0, 0.01, form.get("hue"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.slider("hold", "Hold", 0.0, 1.0, 0.001, form.get("hold"))
	form.slider("pause", "Pause", 0.0, 1.0, 0.001, form.get("pause"))
	form.slider("delay", "Delay", 0.0, 1.0, 0.001, form.get("delay"))
	form.finnish()

def init():
	config["hue"] = 0.0
	config["saturation"] = 1.0
	config["value"] = 1.0
	config["hold"] = 0.0
	config["pause"] = 0.0
	config["delay"] = 0.0

def run():
	while True:
		for b in range(0, 100):
			if(stop): return
			fill(config["hue"], config["saturation"], (config["value"] * (b/100.0)))
			
		time.sleep(config["hold"])
		for b in range(100, 0, -1):
			if(stop): return
			fill(config["hue"], config["saturation"], (config["value"] * (b/100.0)))
			
		time.sleep(config["pause"])

def fill(hue, sat, val):
	for i in range(0, strip.length):
			strip.hsv(hue, sat, val)
	strip.show()
	time.sleep(config["delay"])