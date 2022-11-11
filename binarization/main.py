from functions import *
from skimage.morphology import *
import cv2;

# ESCOLHER IMAGEM
image_name = 'JPCNN001'

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
image = cv2.imread(f'projeto_PDI/images-base/{image_name}.png')

# REALIZAÇÃO DO PROCESSAMENTO DA IMAGEM
imagem_binarizada = binarização(image)
imagem_preenchida = preenchimento_imagem(imagem_binarizada)
imagem_subtraida = remocao_de_ruido(imagem_binarizada, imagem_preenchida)
imagem_final = operacoes_morfologicas(imagem_subtraida)

# EXIBIÇÃO DA IMAGEM
cv2.imshow("output", imagem_final)

cv2.imwrite(f'projeto_PDI/images-result/{image_name}.png', imagem_final)
cv2.waitKey(0)
