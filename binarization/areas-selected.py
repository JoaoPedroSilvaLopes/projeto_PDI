from tkinter import Image
from skimage import *
import cv2;

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 

image = cv2.imread('images-base/JPCNN001.png')

# # tamanho do lado da região é de 146px
# # x: 5 - 6 | y: 3 - 4
# #cv2.rectangle(img=image, pt1=(700, 604), pt2=(846, 750), color=(0,0,0), thickness=2)
# subimg1 = image[700:846, 604:750]

# # x: 2 - 3 | y: 4 - 5
# #cv2.rectangle(img=image, pt1=(262, 750), pt2=(408, 896), color=(0,0,0), thickness=2)
# subimg2 = image[262:408, 750:896]

# # x: 4 - 5 | y: 4 - 5
# #cv2.rectangle(img=image, pt1=(554, 750), pt2=(700, 896), color=(0,0,0), thickness=2)
# subimg3 = image[554:700, 750:896]

# # x: 3 - 4 | y: 5 - 6
# #cv2.rectangle(img=image, pt1=(408, 896), pt2=(554, 1042), color=(0,0,0), thickness=2)
# subimg4 = image[408:554, 896:1042]

# # x: 4 - 5 | y: 6 - 7
# #cv2.rectangle(img=image, pt1=(554, 1042), pt2=(700, 1188), color=(0,0,0), thickness=2)
# subimg5 = image[554:700, 1042:1188]

# # x: 3 - 4 | y: 7 - 8
# #cv2.rectangle(img=image, pt1=(408, 1188), pt2=(554, 1334), color=(0,0,0), thickness=2)
# subimg6 = image[408:554, 1188:1334]

cv2.rectangle(img=image, pt1=(680, 620), pt2=(820, 760), color=(0,0,0), thickness=2)
subimg1 = image[680:820, 620:760]

# x: 2 - 3 | y: 4 - 5
cv2.rectangle(img=image, pt1=(260, 760), pt2=(400, 900), color=(0,0,0), thickness=2)
subimg2 = image[260:400, 760:900]

# x: 4 - 5 | y: 4 - 5
cv2.rectangle(img=image, pt1=(540, 760), pt2=(680, 900), color=(0,0,0), thickness=2)
subimg3 = image[540:680, 760:900]

# x: 3 - 4 | y: 5 - 6
cv2.rectangle(img=image, pt1=(400, 900), pt2=(540, 1040), color=(0,0,0), thickness=2)
subimg4 = image[400:540, 900:1040]

# x: 4 - 5 | y: 6 - 7
cv2.rectangle(img=image, pt1=(540, 1040), pt2=(680, 1180), color=(0,0,0), thickness=2)
subimg5 = image[540:680, 1040:1180]

# x: 3 - 4 | y: 7 - 8
cv2.rectangle(img=image, pt1=(400, 1180), pt2=(540, 1320), color=(0,0,0), thickness=2)
subimg6 = image[400:540, 1180:1320]

grayScaleAreas = sorted([
  round(subimg1.mean()), 
  round(subimg2.mean()), 
  round(subimg3.mean()), 
  round(subimg4.mean()), 
  round(subimg5.mean()), 
  round(subimg6.mean())
])

print(grayScaleAreas)

# deletar primeiro e ultimo elemento do array
del grayScaleAreas[5]
del grayScaleAreas[0]

# fazer a média dos 4 valores restantes e arrendonda-lo
limiar_m = round(sum(grayScaleAreas) / 4)

print(limiar_m)

th, imagem_binarizada = cv2.threshold(image, limiar_m, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("output", image)
cv2.waitKey(0)
