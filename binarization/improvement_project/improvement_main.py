from improvement_functions import *
import cv2;

# ESCOLHER IMAGEM
image_name = 'JPCNN003'
#image_name = 'JPCLN001'

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
image = cv2.imread(f'images-base/{image_name}.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# EXIBIÇÃO DA IMAGEM
binarizada = binarização_melhorada(image)
preenchida = preenchimento_imagem_melhorada(binarizada)
subtraida = remocao_de_ruido_melhorada(binarizada, preenchida)
imagem_final = operacoes_morfologicas_melhorada(subtraida)

#final = cv2.hconcat([image, binarizada, preenchida, subtraida, imagem_final])
final = cv2.hconcat([image, binarizada, preenchida])

cv2.imshow("output", final)
cv2.imwrite(f'images-result/{image_name}.png', imagem_final)
cv2.waitKey(0)
