from functions import *
from skimage.morphology import *
import cv2;

# ESCOLHER IMAGEM
image_name = 'JPCNN003'

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
image = cv2.imread(f'images-base/{image_name}.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# REALIZAÇÃO DO PROCESSAMENTO DA IMAGEM
binarizada = binarização(image)
preenchida = preenchimento_imagem(binarizada)
subtraida = remocao_de_ruido(binarizada, preenchida)
imagem_final = operacoes_morfologicas(subtraida)

#final = cv2.hconcat([image, binarizada, preenchida, subtraida, imagem_final])
final = cv2.hconcat([image, binarizada, preenchida])

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", final)
cv2.imwrite(f'images-result/{image_name}.png', imagem_final)
cv2.waitKey(0)
