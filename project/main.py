from improvement_functions import *
from functions import *
import cv2;

from skimage.util import invert
from skimage.exposure import *
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
  #if image_name == 'JPCNN001':
    # CARREGAMENTO DA IMAGEM
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)

    raw_image = np.fromfile(f'images-base/{image_name}.IMG', dtype=">i2").reshape((2048, 2048)).astype('uint16')
    raw_image = rescale_intensity(raw_image, in_range='uint12', out_range='uint16')
    raw_image = invert(raw_image)

    # PROCESSAR DOIS MÉTODOS
    imagem_original = processar_imagem(raw_image)
    #imagem_melhorada = processar_imagem_melhorada(raw_image)

    # GUARDAR EM ARRAY
    final = cv2.hconcat([imagem_original])
    final_image_array.append(final)

resultado = cv2.vconcat(final_image_array)

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", resultado)
cv2.waitKey(0)
