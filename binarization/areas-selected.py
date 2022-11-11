from tkinter import Image
from skimage.morphology import *
import copy
import cv2;

# REALIZAR A LIMIARIZAÇÃO

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 

image = cv2.imread('projeto_PDI/images-base/JPCNN001.png')
image_real = copy.deepcopy(image)

cv2.rectangle(img=image_real, pt1=(680, 620), pt2=(820, 760), color=(0,0,0), thickness=2)
subimg1 = image[680:820, 620:760]

# x: 2 - 3 | y: 4 - 5
cv2.rectangle(img=image_real, pt1=(260, 760), pt2=(400, 900), color=(0,0,0), thickness=2)
subimg2 = image[260:400, 760:900]

# x: 4 - 5 | y: 4 - 5
cv2.rectangle(img=image_real, pt1=(540, 760), pt2=(680, 900), color=(0,0,0), thickness=2)
subimg3 = image[540:680, 760:900]

# x: 3 - 4 | y: 5 - 6
cv2.rectangle(img=image_real, pt1=(400, 900), pt2=(540, 1040), color=(0,0,0), thickness=2)
subimg4 = image[400:540, 900:1040]

# x: 4 - 5 | y: 6 - 7
cv2.rectangle(img=image_real, pt1=(540, 1040), pt2=(680, 1180), color=(0,0,0), thickness=2)
subimg5 = image[540:680, 1040:1180]

# x: 3 - 4 | y: 7 - 8
cv2.rectangle(img=image_real, pt1=(400, 1180), pt2=(540, 1320), color=(0,0,0), thickness=2)
subimg6 = image[400:540, 1180:1320]

grayScaleAreas = sorted([
  round(subimg1.mean()), 
  round(subimg2.mean()), 
  round(subimg3.mean()), 
  round(subimg4.mean()), 
  round(subimg5.mean()), 
  round(subimg6.mean())
])

# deletar primeiro e ultimo elemento do array
del grayScaleAreas[5]
del grayScaleAreas[0]

# ENCONTRANDO O LIMIAR DA BINARIZAÇÃO
limiar_m = round(sum(grayScaleAreas) / 4)

# REALIZAÇÃO DA BINARIZAÇÃO
th, imagem_binarizada_inicial = cv2.threshold(image, limiar_m, 255, cv2.THRESH_BINARY_INV)

# ETAPA TORNAR 50px EM PIXEIS PRETOS,
imagem_binarizada_preenchida = copy.deepcopy(imagem_binarizada_inicial)

# PINTAR PARTE DE CIMA DA IMAGEM
imagem_binarizada_preenchida[0:50, 0:2048] = (0, 0, 0)
# PINTAR LADO ESQUERDO DA IMAGEM
imagem_binarizada_preenchida[0:2048, 0:50] = (0, 0, 0)
# PINTAR PARTE DE BAIXO DA IMAAGEM
imagem_binarizada_preenchida[0:2048, 1998:2048] = (0, 0, 0)
# PINTAR LADO DIREITO DA IMAGEM
imagem_binarizada_preenchida[1998:2048, 0:2048] = (0, 0, 0)

# LAÇOS FORs PARA PREENCHIMENTO DA IMAGEM
for i in range(50, 1998):
  for j in range(50, 1998):
    if imagem_binarizada_preenchida[j, i, 0] == 0:
      break
    else:
      imagem_binarizada_preenchida[j, i]=[0,0,0]
  
  for j in reversed(range(50, 1998)):
    if imagem_binarizada_preenchida[j, i, 0] == 0:
      break
    else:
      imagem_binarizada_preenchida[j, i]=[0,0,0]

# REMOÇÃO DE RUÍDO APÓS O PREENCHIMENTO
imagem_ruido = cv2.subtract(imagem_binarizada_inicial, imagem_binarizada_preenchida)

# REALIZAÇÃO DA DILATAÇÃO COM 3 ELEMENTOS ESTRUTURANTES
imagem_ruido_dilatado = copy.deepcopy(imagem_ruido)

imagem_ruido_dilatado = cv2.dilate(imagem_ruido_dilatado, disk(60))
imagem_ruido_dilatado = cv2.dilate(imagem_ruido_dilatado, rectangle(30, 10))
imagem_ruido_dilatado = cv2.dilate(imagem_ruido_dilatado, rectangle(10, 30))

# OBTENÇÃO DA IMAGEM RESULTADO PELA SUBTRAÇÃO DA IMAGEM BINARIZADA PELO RUIDO DILATADO
imagem_subtraida = cv2.subtract(imagem_binarizada_inicial, imagem_ruido_dilatado)

# REALIZAÇÃO DE OPERAÇÕES MORFOLÓGICAS DE FECHAMENTO
imagem_subtraida = cv2.morphologyEx(imagem_subtraida, cv2.MORPH_CLOSE, square(35))
imagem_subtraida = cv2.morphologyEx(imagem_subtraida, cv2.MORPH_CLOSE, disk(35))

# REALIZAÇÃO DO AJUSTE DAS REGIÕES ACIMA DAS BASES PULMONARES
imagem_subtraida[0:1638, 0:2048] = cv2.dilate(imagem_subtraida[0:1638, 0:2048], rectangle(40, 2))
imagem_subtraida[0:1638, 0:2048] = cv2.dilate(imagem_subtraida[0:1638, 0:2048], octagon(17, 17))

imagem_subtraida = cv2.morphologyEx(imagem_subtraida, cv2.MORPH_CLOSE, disk(25))

cv2.imshow("output", imagem_subtraida)

#cv2.imshow("output", image)
#cv2.imshow("output", imagem_binarizada_inicial)

cv2.waitKey(0)
