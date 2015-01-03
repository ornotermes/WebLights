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
