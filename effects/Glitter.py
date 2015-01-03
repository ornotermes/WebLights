from random import *

def show():
	form.start()
	form.slider("hue", "Hue", 0.0, 1.0, 0.01, form.get("hue"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.slider("density", "Density", 0.5, 1.0, 0.001, form.get("density"))
	form.finnish()

def init():
	config["hue"] = 0.0
	config["saturation"] = 0.0
	config["value"] = 1.0
	config["density"] = 0.502

def run():
	while True:
		for i in range(0, strip.length):
			if(stop): return
			r = round((random() * config["density"]), 0)
			strip.HSV(config["hue"], config["saturation"], config["value"] * r)

		strip.Show()