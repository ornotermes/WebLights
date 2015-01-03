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
		for l in [0, strip.length / 2]:
			for m in range(0, 3):
				for i in range(0, strip.length):
					if(stop): return
					if( i in range(0 + l, strip.length / 2 + l) ): strip.RGB( 0, 0, 1)
					else: strip.RGB( 0, 0, 0)
				strip.Show()
				time.sleep(0.02)
				strip.Clear()
				strip.Show()
				time.sleep(0.04)
			time.sleep(0.2)
