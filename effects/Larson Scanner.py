def show():
	form.start()
	form.slider("hue", "Hue", 0.0, 1.0, 0.01, form.get("hue"))
	form.slider("saturation", "Saturation", 0.0, 1.0, 0.01, form.get("saturation"))
	form.slider("value", "Value", 0.0, 1.0, 0.01, form.get("value"))
	form.finnish()

def init():
	config["hue"] = 0.0
	config["saturation"] = 1.0
	config["value"] = 1.0
	
def run():
	while True:
		for d in [0, 1]:
			for m in range(0, strip.length):
				for n in range(0, strip.length):
					if stop: return
					v = abs( (d*strip.length) - m)
					if( n == v ) : strip.HSV( config["hue"], config["saturation"], config["value"] * 1.0 )
					if( n == v-1 and v < strip.length-1) : strip.HSV( config["hue"], config["saturation"], config["value"] * 0.5 )
					if( n == v-2 and v < strip.length-2) : strip.HSV( config["hue"], config["saturation"], config["value"] * 0.25 )
					if( n == v-3 and v < strip.length-3) : strip.HSV( config["hue"], config["saturation"], config["value"] * 0.125 )
					if( n == v-4 and v < strip.length-4) : strip.HSV( config["hue"], config["saturation"], config["value"] * 0.0625 )
					else : strip.HSV( config["hue"], config["saturation"], 0.0 )

				strip.Show()
