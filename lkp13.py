import numpy
import cv2

imagesMtx = cv2.imread("a330.jpeg")

shape = imagesMtx.shape
canvas_a = numpy.zeros((shape[1],shape[0],3),numpy.uint8)

for i in range(shape[1]):
    for j in range(shape[0]):
        b, g, r = imagesMtx[j,i]
        canvas_a.itemset((i,j,0), b)
        canvas_a.itemset((i,j,1), g)
        canvas_a.itemset((i,j,2), r)


cv2.imshow("Gambar", canvas_a)
cv2.waitKey(0)
