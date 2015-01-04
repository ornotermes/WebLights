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

def run():
	while True:
		for s in [0,2]:
			for d in [0, 1]:
				for b in range(0, 50):
					f = abs( d - b/50.0 )
					c = s
					for i in range(0, strip.length):
						if stop: return
						if(c == 0):
							strip.rgb(1, 0.8, 0.5)
						if(c == 1):
							strip.rgb(f, 0, 0)
						if(c == 2):
							strip.rgb(1, 0.8, 0.5)
						if(c == 3):
							strip.rgb(0, f, 0)

						c+=1
						if(c >= 4): c = 0

					strip.show()
