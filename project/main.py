from improvement_functions import *
from functions import *
import cv2;

# ARRAY DAS IMAGENS
image_array = [
  'JPCNN001',
  'JPCNN002',
  'JPCNN003',
  'JPCNN004',
  'JPCNN005',
  'JPCLN001',
  'JPCLN002',
  'JPCLN003',
  'JPCLN004',
  'JPCLN005'
]

final_image_array = []

for image_name in image_array:
  # CARREGAMENTO DA IMAGEM
  cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
  image = cv2.imread(f'images-base/{image_name}.png')
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # PROCESSAR DOIS MÉTODOS
  imagem_original = processar_imagem(image)
  imagem_melhorada = processar_imagem_melhorada(image)

  # SOBRESCREVER A IMAGEM
  cv2.imwrite(f'images-result/{image_name}.png', imagem_melhorada)

  # GUARDAR EM ARRAY
  final = cv2.hconcat([image, imagem_original, imagem_melhorada])
  final_image_array.append(final)

resultado = cv2.vconcat(final_image_array)

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", resultado)
cv2.waitKey(0)
