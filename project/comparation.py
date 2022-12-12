from improvement_functions import *
from functions import *

from skimage.util import invert
from skimage.exposure import *
import cv2;
import matplotlib.pyplot as plt 


# ARRAY DAS IMAGENS
image_array = [
  'JPCNN001',
  'JPCNN003',
  'JPCNN005',
  'JPCNN006',
  'JPCNN008',
  'JPCNN009',
  'JPCNN010',
  'JPCLN006',
  'JPCLN008',
  'JPCLN009'
]

final_image_array = []

ground_truth_image = cv2.imread(f'ground_truths/JPCNN001GT.bmp', cv2.IMREAD_GRAYSCALE)
ground_truth_image = cv2.threshold(ground_truth_image, 127, 255, cv2.THRESH_BINARY)[1]

result_image_original_method = cv2.imread(f'result_images_original_method/JPCNN001.png')

histogram_gt_image = plt.hist(ground_truth_image.ravel(), 255, [0, 255])
histogram_result_image = plt.hist(result_image_original_method.ravel(), 255, [0, 255])

print(histogram_gt_image)
plt.show() 
