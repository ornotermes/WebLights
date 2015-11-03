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

import serial, atexit, colorsys

class strip:
	config = {
		"type":		"",
		"port":		"/dev/ttyACM0",
		"length":	"1",
		"width":	"1",
		"depth":	"1",
		"name":		"Arduino strip"
	}
	
	txBuffer = ""
	txSize = 64
		
	def init(self):
		self.port = str(self.config["port"])
		self.length = int(self.config["length"],0)
		self.width = int(self.config["width"],0)
		self.depth = int(self.config["depth"],0)
		self.name = str(self.config["name"])

		self.serial = serial.Serial(self.port, 115200)
		self.txSize = 5;

	def info(self):
		pass
					
	def add(self, command):
		if(len(self.txBuffer) + len(command) > self.txSize-1):
			self.send()
		self.txBuffer += str(command)
	
	def send(self):
		self.serial.write(self.txBuffer)
		self.txBuffer = ""
		
	def clear(self):
		self.add("c")
	
	def goto(self, pos):
		if pos < self.count:
			self.add("g" + chr(pos))
	
	def set(self, red, green, blue):
		self.add("s" + chr(min(red,255))  + chr(min(green,255))  + chr(min(blue,255)))
		
	def show(self):
		self.add("t")
		self.send()
	
	def rgb(self, red, green, blue):
		self.set(int(red*255), int(green*255), int(blue*255))
		
	def hsv(self, hue, sat, val):
		rgb = colorsys.hsv_to_rgb(hue, sat, val)
		self.rgb(rgb[0], rgb[1], rgb[2])
