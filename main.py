# import pytesseract as tess
# tess.pytesseract.tesseract_cmd= r'D:\tesseract-ocr\tesseract.exe'
# from PIL import Image
# import cv2
#
# img = cv2.imread('testimage.jpeg')
#
#
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# text = tess.pytesseract.image_to_string(img,lang='pan')
#
# print(text)
# cv2.imshow("img",img)
# cv2.waitKey(0)
import numpy as np
import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'D:\tesseract-ocr\tesseract.exe'
from PIL import Image
import cv2

img = cv2.imread('testimage.jpeg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



outer=[]
i=1
y=150
while (i<=(img.shape)[0]):
    image=img[i:y,0:1106];
    cv2.imwrite("data"+str(i)+".jpeg",image)
    text = tess.pytesseract.image_to_string(Image.open("data"+str(i)+".jpeg"), lang='pan')
    if(text):
        outer.append(text.split("\n"))
    i=y;
    y=y+150;
    cv2.imshow("cropped",image)
    cv2.waitKey(0)

for i in outer:
    print(i,"\n")

cv2.imshow("orig",img)
cv2.waitKey(0)




