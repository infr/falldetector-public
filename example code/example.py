import sys

def staticFrameDifference(camera):
	import fig1b
	fig1b.main(camera)

def staticFrameDifferenceThreshold(camera):
	import fig2b
	fig2b.main(camera)

def frameDifference(camera):
	import fig6b
	fig6b.main(camera)

def variationOfAdaptiveBackgrounding(camera):
	import fig7b
	fig7b.main(camera)

def normalDistribution():
	import fig8
	fig8.main()

def boundingBox(camera):
	import fig9b
	fig9b.main(camera)

while 1:
	camera = 0
	print "Select script to run"
	print "1: Fig. 1b - Static Frame Difference"
	print "2: Fig. 2b - Static Frame Difference with threshold"
	print "3: Fig. 6b - Frame Difference"
	print "4: Fig. 7b - A variation of adaptive backgrounding"
	print "5: Fig. 8 - Normal Distribution"
	print "6: Fig. 9b - Bounding box"

	print "0: exit"
	s = raw_input("> ")
	if s == "0":
		sys.exit()
	elif s == "1":
		staticFrameDifference(camera)
	elif s == "2":
		staticFrameDifferenceThreshold(camera)
	elif s == "3":
		frameDifference(camera)
	elif s == "4":
		variationOfAdaptiveBackgrounding(camera)
	elif s == "5":
		normalDistribution()
	elif s == "6":
		boundingBox(camera)
	
