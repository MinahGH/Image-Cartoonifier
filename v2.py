import cv2
import numpy as np
#img=cv2.imread('C:/Users/M3MO/Desktop/lead_720_405.jpg',cv2.IMREAD_GRAYSCALE)

#img=cv2.imread('C:/Users/M3MO/Desktop/lead_720_405.jpg')

#img=cv2.imread('C:/Users/M3MO/Desktop/72886955_402902940380576_2077452964993171456_n.jpg')

#img=cv2.imread('C:/Users/M3MO/Desktop/71582753_465347337437409_4099515231418449920_n.jpg')

#img=cv2.imread('C:/Users/M3MO/Desktop/72598980_1334692206700384_3196631806363303936_n.jpg')
img=cv2.imread('C:/Users/M3MO/Desktop/test.PNG')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
median = cv2.medianBlur(gray,7)
cv2.imshow('Smoothed Gray',median)
cv2.waitKey(0)
cv2.destroyAllWindows()
#la=cv2.Laplacian(median , ksize =1,cv2.CV_8UC1)
#la=cv2.Laplacian(median , ksize =3,cv2.CV_8UC1)
la = cv2.Laplacian(median,cv2.CV_8UC1,ksize = 5,scale = 1,delta = 0)
print(la)
cv2.imshow('Laplacian filter',la)
cv2.waitKey(0)
cv2.destroyAllWindows()
#ret3,th3 = cv2.threshold(la,125,255,cv2.THRESH_BINARY) 
ret3,th3 = cv2.threshold(la,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
cv2.imshow('Laplacian after threshold',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()


th4 = th3
print(th3.shape[0])
print(th3.shape[1])
for i in range(0,th3.shape[0]):
    for j in range(0,th3.shape[1]):
        if(th3[i][j]==0):
            th4[i][j]=255
        else:
            th4[i][j]=0
        

cv2.imshow('after fliping',th4)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(0,6):
    bi = cv2.bilateralFilter(img, d=9, sigmaColor=9, sigmaSpace=7)

#bi=cv2.bilateralFilter(img,d=15 ,sigmaColor=70 ,sigmaSpace=70)
	
cv2.imshow('bilateral filter',bi)
cv2.waitKey(0)
cv2.destroyAllWindows()
mask = np.zeros_like(img)

print(th3.shape)
print(bi.shape)
#th3.reshape(bi.shape[0],bi.shape[1],3)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th4 = cv2.cvtColor(th4, cv2.COLOR_GRAY2RGB)
#res = th3  bi
#res=cv2.bitwise_and(th4,bi)
res=cv2.bitwise_and(bi,bi,mask=th3)
cv2.imshow('cartonized',res)
cv2.waitKey(0)
cv2.destroyAllWindows()









