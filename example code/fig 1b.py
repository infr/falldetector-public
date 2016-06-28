import cv2
camera = cv2.VideoCapture(0)
_, backgroundFrame = camera.read()
backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
while 1:
	_, currentFrame = camera.read()
	currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
	foreground = cv2.absdiff(backgroundFrame, currentFrame)
	cv2.imshow("foreground", foreground)