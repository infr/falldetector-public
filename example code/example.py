def staticFrameDifference(camera):
	import fig1b
	fig1b.go(camera)

def staticFrameDifferenceThreshold(camera):
	import fig2b
	fig2b.go(camera)

def frameDifference(camera):
	import fig6b
	fig6b.go(camera)

def variationOfAdaptiveBackgrounding(camera):
	import fig7b
	fig7b.go(camera)

while 1:
	camera = 0
	print "Select script to run"
	print "1: Fig. 1b - Static Frame Difference"
	print "2: Fig. 2b - Static Frame Difference with threshold"
	print "3: Fig. 6b - Frame Difference"
	print "4: Fig. 7b - A variation of adaptive backgrounding"
	s = raw_input("> ")
	if s == "1":
		staticFrameDifference(camera)
	elif s == "2":
		staticFrameDifferenceThreshold(camera)
	elif s == "3":
		frameDifference(camera)
	elif s == "4":
		variationOfAdaptiveBackgrounding(camera)
	
