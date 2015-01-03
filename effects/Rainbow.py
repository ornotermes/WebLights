def run():
	while True:
		for l in range(0, strip.length):
			for i in range(0, strip.length):
				if stop: return
				hue = (1.0/strip.length)*(l)
				hue += (1.0/strip.length)*(i)
				if hue > 1.0:
					hue -= 1
				strip.HSV(hue, 1, 1)

			strip.Show()