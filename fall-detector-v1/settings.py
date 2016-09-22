# Fall detector settings class
#
#
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

class Settings(object):
	
	def __init__(self):
		self.minArea = 50*50 # minimum area to be considered as a person
		self.thresholdLimit = 20
		self.dilationPixels = 30
		self.useGaussian = 1 # yes/no (boolean)
		self.gaussianPixels = 31
		self.movementMaximum = 75 # amount to move to still be the same person
		self.movementMinimum = 3 # minimum amount to move to not trigger alarm
		self.movementTime = 50 # number of frames after the alarm is triggered
		self.place = 'Haaga-Helia testi'