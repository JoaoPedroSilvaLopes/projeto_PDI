from skimage.morphology import *
import copy
import cv2;

# ESTA OK
def processar_imagem_melhorada(image):
  binarizada = binarização_melhorada(image)
  preenchida = preenchimento_imagem_melhorada(binarizada)
  imagem_final = operacoes_morfologicas_melhorada(preenchida)

  return imagem_final

# ESTA OK
def pre_processamento(img):
  # FILTRAR USANDO CONTORNOS E REMOVENDO CONTORNOS PEQUENOS
  cnts = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]

  for c in cnts:
    area = cv2.contourArea(c)
    if area < 49000:
      cv2.drawContours(img, [c], -1, (0), -1)

  img = cv2.morphologyEx(img, cv2.MORPH_OPEN, disk(5))

  return img

# ESTA OK
def binarização_melhorada(img_real):
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (150, 150))
  topHat = cv2.morphologyEx(img_real, cv2.MORPH_TOPHAT, kernel)
  bottomHat = cv2.morphologyEx(img_real, cv2.MORPH_BLACKHAT, kernel)
  img = img_real + topHat - bottomHat

  img = cv2.equalizeHist(img)

  binarizada = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
  img_result = pre_processamento(binarizada)

  return img_result

# ESTA OK
def preenchimento_imagem_melhorada(img_inicial):
  img = copy.deepcopy(img_inicial)

  # ETAPA TORNAR 75px DAS BORDAS EM PIXEIS PRETOS
  img[0:75, 0:2048] = (0)
  img[0:2048, 0:75] = (0)
  img[0:1973, 1973:2048] = (0)
  img[1973:2048, 0:2048] = (0)

  # PREECHIMENTO HORIZONTAL DOS PIXELS BRANCOS PARA PIXELS PRETOS
  for i in range(75, 1973):
    for j in range(75, 1973):
      if img[i, j] == 0:
        break
      else:
        img[i, j] = 0
    
    for j in reversed(range(75, 1973)):
      if img[i, j] == 0:
        break
      else:
        img[i, j] = 0

  img = pre_processamento(img)
    
  return img

# ESTA OK
def operacoes_morfologicas_melhorada(img):
  img = cv2.morphologyEx(img, cv2.MORPH_OPEN, rectangle(20, 2))
  img = pre_processamento(img)

  # REALIZAÇÃO DE OPERAÇÕES MORFOLÓGICAS DE FECHAMENTO
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, square(35))
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(35))

  # REALIZAÇÃO DO AJUSTE DAS REGIÕES ACIMA DAS BASES PULMONARES
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], rectangle(40, 2))
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], octagon(17, 17))

  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(25))

  return img
