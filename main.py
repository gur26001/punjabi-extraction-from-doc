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

import os
from  googletrans import Translator
import pytesseract as tess
tess.pytesseract.tesseract_cmd= r'D:\tesseract-ocr\tesseract.exe'
from PIL import Image
import cv2

img = cv2.imread('testimage.jpeg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


path = "./output"
os.chdir(path)

outer=[]
i=1
y=150
k=1
while (i<=(img.shape)[0]):
    image=img[i:y,0:1106];
    cv2.imwrite("data.jpeg",image)
    text = tess.pytesseract.image_to_string(Image.open("data.jpeg"), lang='pan')
    arr=text.split(" ") and text.split("\n")
    print(arr[0])
    translator = Translator()

    punjabitoeng= translator.translate(str(arr[0]),dest="en")
    folder = str(k)+"c"+str(punjabitoeng.text)
    os.makedirs(folder)
    cv2.imwrite(str(folder)+"/d"+str(punjabitoeng.text)+str(k)+ ".jpeg", image)
    if(text):
        outer.append(text.split("\n"))
    i=y;
    y=y+150;
    cv2.imshow("cropped",image)
    cv2.waitKey(1)
    k+=1

for i in outer:
    print(i,"\n")

cv2.imshow("orig",img)
cv2.waitKey(0)




