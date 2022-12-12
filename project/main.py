from improvement_functions import *
from functions import *
import cv2;
import numpy as np;

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

result_image_array = []
horizontal_array = []

for image_name in image_array:
  # CARREGAMENTO DA IMAGEM
  cv2.namedWindow("output", cv2.WINDOW_NORMAL)

  # CARREGAMENTO DOS GROUND_TRUTH
  ground_truth_image = cv2.imread(f'ground_truths/{image_name}GT.bmp', cv2.IMREAD_GRAYSCALE)
  ground_truth_image = cv2.threshold(ground_truth_image, 127, 255, cv2.THRESH_BINARY)[1]

  # CARREGAMENTO DAS IMAGENS 12 BITS E 8 BITS
  image_12bits = np.fromfile(f'project/images_base/{image_name}.IMG', dtype=">i2").reshape((2048, 2048)).astype('uint16')
  image_8bits = (invert(rescale_intensity(image_12bits, in_range='uint12', out_range='uint16')) / 256).astype('uint8')

  # PROCESSAR DOIS MÉTODOS 
  imagem_original = processar_imagem(image_12bits)
  imagem_melhorada = processar_imagem_melhorada(image_12bits)

  # SOBRESCREVER IMAGENS DE COMPARAÇÃO
  cv2.imwrite(f'comparation/images_result_original_method/{image_name}.png', imagem_original)
  cv2.imwrite(f'comparation/images_result_proposed_method/{image_name}.png', imagem_melhorada)

  # GUARDAR EM ARRAY
  final = cv2.hconcat([image_8bits, ground_truth_image, imagem_original, imagem_melhorada])
  result_image_array.append(final)

# CONCATENAR IMAGENS
horizontal_array.append(cv2.hconcat([result_image_array[0], result_image_array[1]]))
horizontal_array.append(cv2.hconcat([result_image_array[2], result_image_array[3]]))
horizontal_array.append(cv2.hconcat([result_image_array[4], result_image_array[5]]))
horizontal_array.append(cv2.hconcat([result_image_array[6], result_image_array[7]]))
horizontal_array.append(cv2.hconcat([result_image_array[8], result_image_array[9]]))
resultado = cv2.vconcat(horizontal_array)

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", resultado)
cv2.waitKey(0)
