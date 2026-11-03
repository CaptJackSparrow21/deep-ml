import numpy as np

def calculate_brightness(img):
	if len(img) == 0 :
		return -1

	if any(len(row) != len(img[0]) for row in img) :
		return -1

	if len(img[0]) == 0 :
		return -1

	if any(pixel < 0 or pixel > 255 for row in img for pixel in row) :
		return -1

	return round(float(np.mean(img)), 2)
	
