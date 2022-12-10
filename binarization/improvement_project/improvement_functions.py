from skimage.morphology import *
import copy
import cv2;

def binarização_melhorada(img_real):
  topHat = cv2.morphologyEx(img_real, cv2.MORPH_TOPHAT, disk(50))
  bottomHat = cv2.morphologyEx(img_real, cv2.MORPH_BLACKHAT, disk(50))

  img_resultante = img_real + topHat - bottomHat
  img = copy.deepcopy(img_resultante)

  binarizada_1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 977, 5)
  limiar, binarizada_2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  img = binarizada_1 + binarizada_2

  return img

def preenchimento_imagem_melhorada(img_inicial):
  img = copy.deepcopy(img_inicial)

  # ETAPA TORNAR 50px DAS BORDAS EM PIXEIS PRETOS
  img[0:50, 0:2048] = (0)
  img[0:2048, 0:50] = (0)
  img[0:2048, 1998:2048] = (0)
  img[1998:2048, 0:2048] = (0)

  # PREECHIMENTO DOS PIXELS BRANCOS PARA PIXELS PRETOS
  for i in range(50, 1998):
    for j in range(50, 1998):
      if img[j, i] == 0:
        break
      else:
        img[j, i] = 0
    
    for j in reversed(range(50, 1998)):
      if img[j, i] == 0:
        break
      else:
        img[j, i] = 0

  # PREECHIMENTO DOS PIXELS BRANCOS PARA PIXELS PRETOS
  for i in range(50, 1998):
    for j in range(50, 1998):
      if img[i, j] == 0:
        break
      else:
        img[i, j] = 0
    
    for j in reversed(range(50, 1998)):
      if img[i, j] == 0:
        break
      else:
        img[i, j] = 0
    
  return img

def remocao_de_ruido_melhorada(img_inicial, img_binarizada_preenchida):
  # REMOÇÃO DE RUÍDO APÓS O PREENCHIMENTO
  ruido = cv2.subtract(img_inicial, img_binarizada_preenchida)
  
  # REALIZAÇÃO DA DILATAÇÃO COM 3 ELEMENTOS ESTRUTURANTES
  ruido = cv2.dilate(ruido, disk(60))
  ruido = cv2.dilate(ruido, rectangle(30, 10))
  ruido = cv2.dilate(ruido, rectangle(10, 30))

  # OBTENÇÃO DA IMAGEM RESULTADO PELA SUBTRAÇÃO DA IMAGEM BINARIZADA PELO RUIDO DILATADO
  ruido_dilatado = ruido

  return cv2.subtract(img_inicial, ruido_dilatado)

def operacoes_morfologicas_melhorada(img):
  # REALIZAÇÃO DE OPERAÇÕES MORFOLÓGICAS DE FECHAMENTO
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, square(35))
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(35))

  # REALIZAÇÃO DO AJUSTE DAS REGIÕES ACIMA DAS BASES PULMONARES
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], rectangle(40, 2))
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], octagon(17, 17))

  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(25))

  return img
