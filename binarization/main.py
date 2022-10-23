import cv2;

img = cv2.imread('images-base/JPCLN001.png')

th, img_th = cv2.threshold(img, 128, 192, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('images-result/JPCLN001.png', img_th)