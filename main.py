import cv2
import numpy


img=cv2.imread('Face.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 250, 250)
photo_bit = numpy.zeros((10, 10, 3), dtype = 'uint8')
kernel = numpy.ones((5, 5), numpy.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Face',img)
print(photo_bit)
cv2.waitKey(0)
"""video = cv2.VideoCapture(0)
video.set(3, 500)
video.set(4, 300)
while True:
    _, img = video.read()
    cv2.imshow('Video', img)
    cv2.waitKey(1)"""