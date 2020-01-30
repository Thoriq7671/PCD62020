#Muhammmad Alpha Thoriq
#G64170002
#LKP 2 

import numpy
import cv2

imagesMtx = cv2.imread("Lenna.png")

shape = imagesMtx.shape
canvas_a = numpy.zeros((shape[0],shape[1],1),numpy.uint8)

for i in range(shape[0]):
    for j in range(shape[1]):
        b, g, r = imagesMtx[i,j]
        Gray = (r * 0.299 + g * 0.587 + b * 0.114)

        canvas_a.itemset((i,j,0), Gray)



cv2.imshow("Gambar 1", canvas_a)


# no 2
imagesMtx = cv2.imread("Lenna.png")
canvas_a = numpy.zeros((shape[0],shape[1],1),numpy.uint8)

for i in range(shape[0]):
    for j in range(shape[1]):
        b, g, r = imagesMtx[i,j]
        px = (r * 0.299 + g * 0.587 + b * 0.114)
        if px > 125:
            px = 255
        else:
            px = 0
        canvas_a.itemset((i,j,0), px)



cv2.imshow("Gambar 2", canvas_a)


# no 3
imagesMtx = cv2.imread("Lenna.png")
canvas_a = numpy.zeros((shape[0],shape[1],1),numpy.uint8)

for i in range(shape[0]):
    for j in range(shape[1]):
        b, g, r = imagesMtx[i,j]
        px = (r * 0.299 + g * 0.587 + b * 0.114)
        if px > 125:
            px = 125
        else:
            px = 0
        canvas_a.itemset((i,j,0), px)



cv2.imshow("Gambar 3", canvas_a)
cv2.waitKey(0)
