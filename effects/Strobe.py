def show():
	form.start()
	form.slider("hue", "Hue", 0.0, 1.0, 0.01, form.get("hue"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.slider("delay", "Delay", 0.0, 1.0, 0.01, form.get("delay"))
	form.finnish()

def init():
	config["hue"] = 0.0
	config["saturation"] = 0.0
	config["value"] = 1.0
	config["delay"] = 0.1

def run():
	while(1):
		for i in range(0, strip.length):
			if(stop): return
			strip.HSV(config["hue"], config["saturation"], config["value"])
		strip.Show()
	
		for i in range(0, strip.length):
			if(stop): return
			strip.HSV(0.0, 0.0, 0.0)
		strip.Show()
		time.sleep(config["delay"])