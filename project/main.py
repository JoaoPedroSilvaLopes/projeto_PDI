from improvement_functions import *
from functions import *

from skimage.util import invert
from skimage.exposure import *
import cv2;
import numpy as np

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

for image_name in image_array:
  # CARREGAMENTO DA IMAGEM
  cv2.namedWindow("output", cv2.WINDOW_NORMAL)

  # ground_truth_image = cv2.imread(f'ground_truths/{image_name}GT.bmp')
  # teste = cv2.cvtColor(ground_truth_image, cv2.COLOR_GRAY2)

  image_12bits = np.fromfile(f'images-base/{image_name}.IMG', dtype=">i2").reshape((2048, 2048)).astype('uint16')
  image_12bits = rescale_intensity(image_12bits, in_range='uint12', out_range='uint16')
  image_12bits = invert(image_12bits)

  image_8bits = (image_12bits / 256).astype('uint8')

  # PROCESSAR DOIS MÉTODOS
  imagem_original = processar_imagem(image_8bits)
  imagem_melhorada = processar_imagem_melhorada(image_8bits)

  # GUARDAR EM ARRAY
  final = cv2.hconcat([image_8bits, imagem_original, imagem_melhorada])
  final_image_array.append(final)

resultado = cv2.vconcat(final_image_array)

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", resultado)
cv2.waitKey(0)
