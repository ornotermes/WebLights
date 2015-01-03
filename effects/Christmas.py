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
							strip.RGB(1, 0.8, 0.5)
						if(c == 1):
							strip.RGB(f, 0, 0)
						if(c == 2):
							strip.RGB(1, 0.8, 0.5)
						if(c == 3):
							strip.RGB(0, f, 0)

						c+=1
						if(c >= 4): c = 0

					strip.Show()
