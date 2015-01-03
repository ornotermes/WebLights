from random import *

def show():
	form.start()
	form.slider("hue", "Hue", 0.0, 1.0, 0.01, form.get("hue"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.finnish()

def init():
	config["hue"] = 0.1
	config["saturation"] = 0.9
	config["value"] = 1.0

def run():
	while True:
		for i in range(0, strip.length):
			if(stop): return
			r = random()
			strip.HSV(config["hue"], config["saturation"], config["value"] * r)

		strip.Show()
		time.sleep(0.05)
