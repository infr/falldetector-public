# Fall detector video class
# Source: camera (int) or file (string)
#
#
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import time
import cv2
import person
import settings
import webservice

debug = 0

class Video:
	def __init__(self, source):
		self.camera = cv2.VideoCapture(source)
		self.backgroundFrame = None
		self.start = time.time()
		self.settings = settings.Settings()
		self.persons = person.Persons(self.settings.movementMaximum, self.settings.movementMinimum, self.settings.movementTime)
		self.start = time.time()
		self.webservice = webservice.Webservice(self.settings.place)
		self.errorcount = 0
		self.alertLog = []
		self.frameCount = 1

	def nextFrame(self):
		grabbed, self.frame = self.camera.read()
		if not grabbed: # eof
			self.destroyNow()
		self.convertFrame()


	def showFrame(self):
		if debug:
			cv2.imshow("Thresh", self.thresh)
			cv2.imshow("backgroundFrame", self.backgroundFrame)
			cv2.imshow("frameDelta", self.frameDelta)
		cv2.imshow("Feed", self.frame)


	def destroyNow(self):
		self.camera.release()
		cv2.destroyAllWindows()

	def testDestroy(self):
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			self.destroyNow()
			return 1
		else:
			return 0

	def resetbackgroundFrame(self):
		grabbed, self.frame = self.camera.read()
		self.convertFrame()
		self.backgroundFrame = self.currentFrame
		self.persons = person.Persons(self.settings.movementMaximum, self.settings.movementMinimum, self.settings.movementTime)
		self.frameCount = 1
		print 'resetbackgroundFrame'

	def testBackgroundFrame(self):
		key = cv2.waitKey(1) & 0xFF
		if key == ord("n"):
			self.backgroundFrame = None
		if self.backgroundFrame is None:
			self.resetbackgroundFrame()

	def testSettings(self):
		key = cv2.waitKey(1) & 0xFF
		if key == ord("0"):
			self.settings.minArea += 50
			print "minArea: " , self.settings.minArea
		if key == ord("9"):
			self.settings.minArea -= 50
			print "minArea: " , self.settings.minArea
		if key == ord("8"):
			self.settings.dilationPixels += 1
			print "dilationPixels: " , self.settings.dilationPixels
		if key == ord("7"):
			self.settings.dilationPixels -= 1
			print "dilationPixels: " , self.settings.dilationPixels
		if key == ord("6"):
			self.settings.thresholdLimit += 1
			print "thresholdLimit: " , self.settings.thresholdLimit
		if key == ord("5"):
			self.settings.thresholdLimit -= 1
			print "thresholdLimit: " , self.settings.thresholdLimit
		if key == ord("4"):
			self.settings.movementMaximum += 1
			print "movementMaximum: " , self.settings.movementMaximum
		if key == ord("3"):
			self.settings.movementMaximum -= 1
			print "movementMaximum: " , self.settings.movementMaximum
		if key == ord("2"):
			self.settings.movementMinimum += 1
			print "movementMinimum: " , self.settings.movementMinimum 
		if key == ord("1"):
			self.settings.movementMinimum  -= 1
			print "movementMinimum: " , self.settings.movementMinimum 
		if key == ord("o"):
			if self.settings.useGaussian:
				self.settings.useGaussian = 0
				print "useGaussian: off"
				self.resetbackgroundFrame()
			else:
				self.settings.useGaussian = 1
				print "useGaussian: on"
				self.resetbackgroundFrame()
		if key == ord("+"):
			self.settings.movementTime += 1
			print "movementTime: " , self.settings.movementTime
		if key == ord("p"):
			self.settings.movementTime -= 1
			print "movementTime : " , self.settings.movementTime

	def updateBackground(self):
		alpha = (1.0/self.frameCount)
		self.backgroundFrame = cv2.addWeighted(self.currentFrame, alpha, self.backgroundFrame, 1.0-alpha, 0)
		self.frameCount += 1

	def convertFrame (self):
		r = 750.0 / self.frame.shape[1]
		dim = (750, int(self.frame.shape[0] * r))
		self.frame = cv2.resize(self.frame, dim, interpolation = cv2.INTER_AREA)
		self.currentFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
		if self.settings.useGaussian:
			self.currentFrame = cv2.GaussianBlur(self.currentFrame, (self.settings.gaussianPixels, self.settings.gaussianPixels), 0)

	def compare(self):
		# difference between the current frame and backgroundFrame
		self.frameDelta = cv2.absdiff(self.backgroundFrame, self.currentFrame)
		self.thresh = cv2.threshold(self.frameDelta, self.settings.thresholdLimit, 255, cv2.THRESH_BINARY)[1]
		self.thresh = cv2.dilate(self.thresh, None, iterations=self.settings.dilationPixels) # dilate thresh
		(contours, _) = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

		self.persons.tick()

		detectStatus = "idle"

		for contour in contours:
			if cv2.contourArea(contour) < self.settings.minArea:
				continue

			(x, y, w, h) = cv2.boundingRect(contour)

			if self.thresh.shape[1] < w+50 and self.thresh.shape[0] < h+50:
				self.newLightconditions()
				continue

			person = self.persons.addPerson(x, y, w, h)
			color = (0, 255, 0)
			if person.alert:
				color = (0, 0, 255)
				cv2.line(self.frame, (x, y), (x + w, y + h), color, 2)
				cv2.line(self.frame, (x + w, y), (x , y + h), color, 2)
				detectStatus = "Alarm, not moving"
				if not person.alarmReported:
					self.webservice.alarm("not moving", person.id)
					person.alarmReported = 1

			cv2.rectangle(self.frame, (x, y), (x + w, y + h), color, 2)
			cv2.putText(self.frame, "{}".format(cv2.contourArea(contour)), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1)
			cv2.putText(self.frame, "{} : {}".format(person.id, person.lastmoveTime), (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)

		# Hud + fps
		if debug:
			self.end = time.time()
			seconds = self.end - self.start
			fps  = round((1 / seconds), 1)
			self.start = time.time()

			cv2.putText(self.frame, "Status: {}".format(detectStatus), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 140, 255), 1)
	 		cv2.putText(self.frame, "FPS: {}".format(fps), (400, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 140, 255), 1)

	def newLightconditions(self):
		self.errorcount += 1
		if self.errorcount > 10:
	 		time.sleep(1.0)
	 		self.resetbackgroundFrame()
	 		self.errorcount = 0