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

import usb, atexit, colorsys

class strip:
	config = {
		"type":		"",
		"vid":		"0x03eb",
		"pid":		"0x206c",
		"instance": "0",
		"length":	"1",
		"width":	"1",
		"depth":	"1",
		"name":		"LED Strip",
	}
	
	txBuffer = ""
	txSize = 64
		
	def init(self):
		self.vid = int(self.config["vid"],0)
		self.pid = int(self.config["pid"],0)
		self.instance = int(self.config["instance"],0)
		self.length = int(self.config["length"],0)
		self.width = int(self.config["width"],0)
		self.depth = int(self.config["depth"],0)
		self.name = str(self.config["name"])

		self.device = self.getDevice( self.vid, self.pid, self.instance )
		if not self.device:
			exit('No compatible device found!')
			
		self.device.set_configuration()
		self.cfg = self.device.get_active_configuration()
		self.iface = self.cfg[(0,0)]

		#if self.device.is_kernel_driver_active(self.iface):
		#	self.device.detach_kernel_driver(self.iface)

		self.txep = usb.util.find_descriptor(
			self.iface,
			# match the first OUT endpoint
			custom_match = \
			lambda e: \
				usb.util.endpoint_direction(e.bEndpointAddress) == \
				usb.util.ENDPOINT_OUT)

		self.rxep = usb.util.find_descriptor(
			self.iface,
			# match the first OUT endpoint
			custom_match = \
			lambda e: \
				usb.util.endpoint_direction(e.bEndpointAddress) == \
				usb.util.ENDPOINT_IN)

		self.device.reset()

	def info(self):
		pass
    
	def getDevice(self, vid, pid, instance):
		for dev in usb.core.find(find_all=True, idVendor=vid, idProduct=pid):
			if dev.product.startswith(self.name):
				if instance == 0:
					return dev
				else:
					instance -= 1
					
	def Add(self, command):
		if(len(self.txBuffer) + len(command) > self.txSize-1):
			self.Send()
		self.txBuffer += command
	
	def Send(self):
		self.txep.write(self.txBuffer.ljust(self.txSize, "x"))
		self.txBuffer = ""
		
	def Clear(self):
		self.Add("c")
	
	def GoTo(self, pos):
		if pos < self.count:
			self.Add("g" + chr(pos))
	
	def Set(self, red, green, blue):
		self.Add("s" + chr(min(red,255))  + chr(min(green,255))  + chr(min(blue,255)))
		
	def Show(self):
		self.Add("t")
		self.Send()
	
	def RGB(self, red, green, blue):
		self.Set(int(red*255), int(green*255), int(blue*255))
		
	def HSV(self, hue, sat, val):
		rgb = colorsys.hsv_to_rgb(hue, sat, val)
		self.RGB(rgb[0], rgb[1], rgb[2])
