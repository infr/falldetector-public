import sys
import cv2

def main(camera):
	# Fig. 9b - Bounding box
	threshold = 10
	camera = cv2.VideoCapture(camera)
	_, backgroundFrame = camera.read()
	backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
	i = 1
	while 1:
		_, currentFrame = camera.read()
		currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
		foreground = cv2.absdiff(backgroundFrame, currentFrame)
		foreground = cv2.threshold(foreground, threshold, 255, cv2.THRESH_BINARY)[1]
		(contours, _) = cv2.findContours(foreground, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		alpha = (1.0/i)
		backgroundFrame = cv2.addWeighted(currentFrame, alpha, backgroundFrame, 1.0-alpha, 0)
		cv2.imshow("backgroundFrame", backgroundFrame)
		i += 1

		for contour in contours:
			if cv2.contourArea(contour) < (50*50):
				continue
				
			(x, y, w, h) = cv2.boundingRect(contour)
			cv2.rectangle(foreground, (x, y), (x + w, y + h), (0, 0, 255), 2)
			cv2.rectangle(currentFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		cv2.imshow("foreground", foreground)
		cv2.imshow("currentFrame", currentFrame)

		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			cv2.destroyAllWindows()
			camera.release()
			sys.exit()

if __name__ == '__main__':
   main()