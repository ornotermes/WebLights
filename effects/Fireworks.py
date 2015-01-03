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
					strip.HSV(color, 1.0, 1.0)
				else:
					strip.RGB(0.0, 0.0, 0.0)
			strip.Show()
		
		for b in range(100, 0, -1):
			for i in range(0, strip.length):
				if(stop): return
				if (i > (start-r)) & (i < (start+r)):
					if sparkle & int(round(random()*0.6)):
						strip.HSV(1.0, sparkleColor, 1.0)
					else:
						strip.HSV(color, 1.0, b/100.0)
				else:
					strip.RGB(0.0, 0.0, 0.0)
			strip.Show()
			
		for b in range(83, 0, -1):
			for i in range(0, strip.length):
				if(stop): return
				if (i > (start-r)) & (i < (start+r)):
					if sparkle & int(round(random()*(0.6*(b/200.0+0.5)))):
						strip.HSV(1.0, sparkleColor, 1.0)
					else:
						strip.HSV(color, 0.0, 0.0)
				else:
					strip.RGB(0.0, 0.0, 0.0)
			strip.Show()
			
		for i in range(0, strip.length):
			strip.RGB(0.0, 0.0, 0.0)
		strip.Show()