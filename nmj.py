from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np


def sharpen(image, level):
	enhancer = ImageEnhance.Sharpness(image)
	return enhancer.enhance(level)

def jpegify(image, quality, iterations):
	buffer = BytesIO()
	w,h = image.size

	for i in range(iterations):
		image.save(buffer, format='jpeg', quality=quality)
		buffer.seek(0)
		shrunk = image.resize((int(w*0.1), int(h*0.1)))
		shrunk = shrunk.resize((w, h))
		improved = Image.open(buffer)
		improved = Image.blend(improved, shrunk, 0.5)
		improved = sharpen(improved, 5)
		image = improved
	return image


def test():

	fig = plt.figure()
	plt.ion()

	image = Image.open("lorem_ipsum.png")
	for i in range(10):
		image = jpegify(image, 3, 5)
		plt.imshow(image)
		plt.show()
		plt.pause(.001)
	plt.show()
test()

