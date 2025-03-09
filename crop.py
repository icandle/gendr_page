import cv2
import basicsr

x = 100
y = 500



image1 = cv2.imread(r"C:\Users\wyrmy\Downloads\2\F8_Bicubic.png")
image2 = cv2.imread(r"C:\Users\wyrmy\Downloads\2\F8_GenDR.png")

w,h,c=image1.shape

print(w,h)

x = 100 ##w//4
y=0
t2 = h
t1 = min(w,int(h*1920/2800))
if t1 == w:
    x = 0
    t2 = int(h*2800/1920)

crop1 = image1[x:x+t1,y:y+t2]
crop2 = image2[x:x+t1,y:y+t2]

cv2.imwrite(r"C:\Users\wyrmy\Downloads\2\F8_Bicubic_crop.png", crop1)
cv2.imwrite(r"C:\Users\wyrmy\Downloads\2\F8_GenDR_crop.png", crop2)