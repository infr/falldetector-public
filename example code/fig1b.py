import sys
import cv2

def main(camera):
	# Fig. 1b - Static Frame Difference
	camera = cv2.VideoCapture(camera)
	backgroundFrame = camera.read()[1]
	backgroundFrame = cv2.cvtColor(backgroundFrame, cv2.COLOR_BGR2GRAY)
	while 1:
		currentFrame = camera.read()[1]
		currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
		foreground = cv2.absdiff(backgroundFrame, currentFrame)
		cv2.imshow("backgroundFrame", backgroundFrame)
		cv2.imshow("foreground", foreground)

		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			cv2.destroyAllWindows()
			camera.release()
			sys.exit()

if __name__ == '__main__':
   main()