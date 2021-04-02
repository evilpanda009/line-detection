# Import the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_lines(image, lines):
	line_image = np.zeros_like(image)
	if lines is not None:
		for x in range(0, len(lines)):
		  for x1, y1, x2, y2 in lines[x]:
		    cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
	return line_image

# Path of image directory
frame = cv2.imread('line_detection.jpg')


inputImageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(inputImageGray, (4,4))
edges = cv2.Canny(img_blur,100,220,apertureSize = 3)


lines = cv2.HoughLinesP(edges,cv2.HOUGH_PROBABILISTIC, np.pi/180, 30, minLineLength = 30,maxLineGap = 5)

line_image = display_lines(frame, lines)
result = cv2.addWeighted(frame, 0.8, line_image, 1, 1)


cv2.imshow('results', result)
	


cv2.waitKey()
cv2.destroyAllWindows()

