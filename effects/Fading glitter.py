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
	form.slider("hue_min", "Hue min", 0.0, 1.0, 0.01, form.get("hue_min"))
	form.slider("hue_max", "Hue max", 0.0, 1.0, 0.01, form.get("hue_max"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.slider("decay", "Decay", 0.0, 1.0, 0.01, form.get("decay"))
	form.slider("delay", "Delay", 0, 10, 1, form.get("delay"))
	form.finnish()

def init():
	config["hue_min"] = 0.0
	config["hue_max"] = 0.0
	config["saturation"] = 1.0
	config["value"] = 1.0
	config["decay"] = 0.5
	config["delay"] = 1

value = [0.0]
hue = [0.0]

def run():
	global value
	value = [0.0]*strip.length
	global hue
	hue = [0.0]*strip.length
	d = 0
	while True:
		
		value = [config["decay"]*x for x in value]
		
		if (d == 0):
			make_led()
			d = config["delay"]
		else: d -= 1
		
		for n in range(0, strip.length):
			if stop: return
			strip.hsv( hue[n], config["saturation"], value[n] )
		
		strip.show()

def range_hue():
	if ( config["hue_min"] < config["hue_max"] ):
		hmin = config["hue_min"]
		hmax = config["hue_max"]
	else:
		hmin = config["hue_max"]
		hmax = config["hue_min"]
	hdiff = hmax - hmin
	hue = hmin + hdiff * random()
	return hue

def make_led():
	led = int(strip.length * random())
	value[led] = config["value"]
	hue[led] = range_hue()