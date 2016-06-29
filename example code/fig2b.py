import sys
import cv2

def main(camera):
	# Fig. 2b - Static Frame Difference with threshold
	threshold = 100
	camera = cv2.VideoCapture(camera)
	_, backgroundFrame = camera.read()
	backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
	while 1:
		_, currentFrame = camera.read()
		currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
		foreground = cv2.absdiff(backgroundFrame, currentFrame)
		foreground = cv2.threshold(foreground, threshold, 255, cv2.THRESH_BINARY)[1]
		cv2.imshow("backgroundFrame", backgroundFrame)
		cv2.imshow("foreground", foreground)
		
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			cv2.destroyAllWindows()
			camera.release()
			sys.exit()

if __name__ == '__main__':
   main()