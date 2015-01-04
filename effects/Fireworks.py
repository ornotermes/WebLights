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

def run():
	while True:
		radius = 10 + int(random() * ((strip.length/4)-10))
		start = radius + int(random() * (strip.length - radius))
		color = random()
		sparkle = 1
		sparkleColor = round(random())
		
		for r in range(0, radius, 3):
			for i in range(0, strip.length):
				if(stop): return
				if (i > (start-r)) & (i < (start+r)):
					strip.hsv(color, 1.0, 1.0)
				else:
					strip.rgb(0.0, 0.0, 0.0)
			strip.show()
		
		for b in range(100, 0, -1):
			for i in range(0, strip.length):
				if(stop): return
				if (i > (start-r)) & (i < (start+r)):
					if sparkle & int(round(random()*0.6)):
						strip.hsv(1.0, sparkleColor, 1.0)
					else:
						strip.hsv(color, 1.0, b/100.0)
				else:
					strip.rgb(0.0, 0.0, 0.0)
			strip.show()
			
		for b in range(83, 0, -1):
			for i in range(0, strip.length):
				if(stop): return
				if (i > (start-r)) & (i < (start+r)):
					if sparkle & int(round(random()*(0.6*(b/200.0+0.5)))):
						strip.hsv(1.0, sparkleColor, 1.0)
					else:
						strip.hsv(color, 0.0, 0.0)
				else:
					strip.rgb(0.0, 0.0, 0.0)
			strip.show()
			
		for i in range(0, strip.length):
			strip.rgb(0.0, 0.0, 0.0)
		strip.show()
