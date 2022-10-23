import cv2;

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 

image = cv2.imread('images/JPCLN001.png')

areaSelected3 = cv2.rectangle(img=image, pt1=(400, 600), pt2=(500, 700), color=(0,0,0), thickness=2)

areaSelected1 = cv2.rectangle(img=image, pt1=(500, 700), pt2=(600, 800), color=(0,0,0), thickness=2)

areaSelected2 = cv2.rectangle(img=image, pt1=(700, 500), pt2=(800, 600), color=(0,0,0), thickness=2)

areaSelected4 = cv2.rectangle(img=image, pt1=(600, 600), pt2=(700, 700), color=(0,0,0), thickness=2)

areaSelected5 = cv2.rectangle(img=image, pt1=(600, 800), pt2=(700, 900), color=(0,0,0), thickness=2)

areaSelected6 = cv2.rectangle(img=image, pt1=(600, 1000), pt2=(500, 900), color=(0,0,0), thickness=2)

print(areaSelected1)

cv2.imshow("output", image)
cv2.waitKey(0)
