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

def show():
	form.start()
	form.slider("delay", "Delay", 0.0, 0.1, 0.001, form.get("delay"))
	form.check("reverse", "Reverse", form.get("reverse"))
	form.finnish()

def init():
	config["delay"] = 0.0
	config["reverse"] = False

def run():
	while True:
		for l in range(0, strip.length):
			
			if (config["reverse"]):
				lhue = (1.0/strip.length)*(strip.length-l)
			else:
				lhue = (1.0/strip.length)*(l)
				
			for i in range(0, strip.length):
				if stop: return
				hue = lhue + (1.0/strip.length)*(i)
				if hue > 1.0:
					hue -= 1
				strip.hsv(hue, 1, 1)

			strip.show()
			time.sleep(config["delay"])
