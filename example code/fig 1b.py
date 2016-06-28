# Fig. 1b - Static Frame Difference in Python
import cv2
camera = cv2.VideoCapture(0)
backgroundFrame = camera.read()[1]
backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
while 1:
	currentFrame = camera.read()[1]
	currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
	foreground = cv2.absdiff(backgroundFrame, currentFrame)
	cv2.imshow("backgroundFrame", backgroundFrame)
	cv2.imshow("foreground", foreground)