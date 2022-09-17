# Authors: 
# David Benavides Naranjo - ?
# Reyner Marxell Arias Muñoz - 2019156290
# Date: 16-9-2022
# Course: IC-8046 Introduction to Pattern Recognition

# Necessary imports
import cv2
import pathlib
import math
import numpy

print("Welcome to Lab03, please type the image path:")
imagePath = input()

image = cv2.imread(str(imagePath), cv2.IMREAD_GRAYSCALE)
height, width, numberChannels = image.shape

xAxis = numpy.random.randint(0, size=(height, width)).astype('uint8')
yAxis = numpy.random.randint(0, size=(height, width)).astype('uint8')
superpose = numpy.random.randint(0, size=(height, width)).astype('uint8')

grayXAxis = cv2.cvtColor(xAxis, cv2.COLOR_GRAY2BGR)
grayYAxis = cv2.cvtColor(yAxis, cv2.COLOR_GRAY2BGR)
graySuperpose = cv2.cvtColor(superpose, cv2.COLOR_GRAY2BGR)

for i in range(0, len(image)):
    i = 0

"""cv2.imshow("Prueba", image)
cv2.waitKey(0)"""

