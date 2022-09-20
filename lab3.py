# Authors: 
# David Benavides Naranjo - 2019018297
# Reyner Marxell Arias Muñoz - 2019156290
# Date: 16-9-2022
# Course: IC-8046 Introduction to Pattern Recognition

# Necessary imports
import cv2
import pathlib
import math
from matplotlib import pyplot as plt
import numpy

#This integer is crucial for defining the limit of the result of the subtraction used to define edges
limit = 22

print("Welcome to Lab03, please type the image path:")
imagePath = input()

image = cv2.imread(str(imagePath), cv2.IMREAD_GRAYSCALE)
height, width = image.shape

xAxis = image.copy()
yAxis = image.copy()
superpose = image.copy()

#This section subtracts the value of each pixel with the previous pixel in the image for the x axis and the bottom pixel for the y axis,
#the result will be added to the respective image.
for i in range(0, height):
    for j in range(0, width):
        if j == 0 or i == 0:
            xAxis[i][j] = 0
            yAxis[i][j] = 0
        else:
            substractionY = abs(int(image[i][j])-int(image[i-1][j]))
            if substractionY >= limit:
                yAxis[i][j] = 255
            else:
                yAxis[i][j] = 0
            
            substractionX = abs(int(image[i][j])-int(image[i][j-1]))
            if substractionX >= limit:
                xAxis[i][j] = 255
            else:
                xAxis[i][j] = 0

#Here, both images are compared pixel by pixel, if the values are the same in each image
#then the value in the new image will be 0, and 255 if they are different.
for i in range(0, height):
    for j in range(0, width):
        if int(xAxis[i][j]) == int(yAxis[i][j]):
            superpose[i][j] = 0
        else:
            superpose[i][j] = 255

#This section saves the three new images.
cv2.imwrite("xAxis.jpg", xAxis)
cv2.imwrite("yAxis.jpg", yAxis)
cv2.imwrite("superpose.jpg", superpose)