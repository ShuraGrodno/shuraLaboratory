import cv2
import numpy

# img=cv2.imread('Face.jpg', cv2.IMREAD_GRAYSCALE) # Загрузить изображение в черно-белом цвете
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) # Увеличить или уменьшить изображение
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # преобразование изображения в черно-белый цвет
# img = cv2.GaussianBlur(img, (5, 5), 0) # Размытие изображения
# img = cv2.Canny (img, 100, 150) # Оставляем только черный и белый цвет, без оттенков
# kernel = numpy.ones((5, 5), numpy.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations=1)

# print(cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0][0])

# faces=cv2.CascadeClassifier('faces_detect.xml')
# rezult=faces.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3)
#
# for (x,y,w,h) in rezult:
#     cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),thickness=2)
#
# cv2.imshow('Face',img)
#
# if cv2.waitKey(0) == ord('q'):
#     cv2.destroyAllWindows()
video = cv2.VideoCapture(0)
video.set(3, 500)
video.set(4, 300)
faces=cv2.CascadeClassifier('faces_detect.xml')
cikle = True
while cikle:
    _, img = video.read()
    rezult=faces.detectMultiScale(img, scaleFactor=1.2, minNeighbors=1)
    for (x, y, w, h) in rezult:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),thickness=2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) == ord('q'):
        cikle = False
        cv2.destroyAllWindows()