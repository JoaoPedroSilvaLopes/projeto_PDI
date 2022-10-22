import cv2;

img = cv2.imread('images/JPCLN001.png')

im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

print(th)
# 128.0

cv2.imwrite('images/JPCLN001.png', im_gray_th_otsu)