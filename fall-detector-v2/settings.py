# Fall detector settings class
#
#
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

class Settings(object):
	
	def __init__(self):
		self.debug = 1 # boolean
		self.source = 0 # camera source
		self.bsMethod = 1 # listed in bs.py
		self.MOG2learningRate = 0.001
		self.MOG2shadow = 0
		self.MOG2history = 100
		self.MOG2thresh = 20
		self.minArea = 50*50 # minimum area to be considered as a person
		self.thresholdLimit = 50
		self.dilationPixels = 30
		self.useGaussian = 0 # boolean
		self.useBw = 1 # boolean
		self.useResize = 1 # boolean
		self.gaussianPixels = 31
		self.movementMaximum = 75 # amount to move to still be the same person
		self.movementMinimum = 3 # minimum amount to move to not trigger alarm
		self.movementTime = 50 # number of frames after the alarm is triggered
		self.location = 'Viikintie 1'
		self.phone = '01010101010'