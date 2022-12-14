# opencv_full_lower_upper_Detection.py : 세개 cascade 대해 출력
import numpy as np
import cv2
from matplotlib import pyplot as plt


filename = "people_4.jpg"
# 예측할 그림 가져오기, gray convert
image1 = cv2.imread('images/'+filename)     
grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread('images/'+filename)     
grayImage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

image3 = cv2.imread('images/'+filename)     
grayImage3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)


# cascade xml 파일 선택
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# 10 = 검출한 사각형 사이 최소 간격, body에 x,y,w,h가 여러개 저장됨.
body = body_cascade.detectMultiScale(grayImage1, 1.01, 10, 0, minSize=(100, 100))

for (x,y,w,h) in body :         
    cv2.rectangle(image1,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 1)
plt.imshow(image1, cmap='gray')



# cascade xml 파일 선택
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
body = body_cascade.detectMultiScale(grayImage1, 1.01, 10, 0, minSize=(100, 100))

for (x,y,w,h) in body :        
    cv2.rectangle(image2,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 2)
plt.imshow(image2, cmap='gray')



# cascade xml 파일 선택
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
body = body_cascade.detectMultiScale(grayImage1, 1.01, 10, 0, minSize=(100, 100))

for (x,y,w,h) in body : 
    cv2.rectangle(image3,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 3)
plt.imshow(image3, cmap='gray')


plt.show()