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
  # Filter using contour area and remove small noise
  cnts = cv2.findContours(img[0:512, 0:2048], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  for c in cnts:
    area = cv2.contourArea(c)
    if area < 32000:
      cv2.drawContours(img, [c], -1, (0), -1)

  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
  close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations = 5)

  return img

# ESTA OK
def binarização_melhorada(img_real):
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 50))
  topHat = cv2.morphologyEx(img_real, cv2.MORPH_TOPHAT, kernel)
  bottomHat = cv2.morphologyEx(img_real, cv2.MORPH_BLACKHAT, kernel)
  img = img_real + topHat - bottomHat

  binarizada_1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 1077, 5)
  binarizada_1 = pre_processamento(binarizada_1)

  #binarizada_2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

  return binarizada_1

# ESTA OK
def preenchimento_imagem_melhorada(img_inicial):
  img = copy.deepcopy(img_inicial)

  # ETAPA TORNAR 75px DAS BORDAS EM PIXEIS PRETOS
  img[0:75, 0:2048] = (0)
  img[0:2048, 0:75] = (0)
  img[0:1973, 1973:2048] = (0)
  img[1973:2048, 0:2048] = (0)

  # PREECHIMENTO VERTICAL DOS PIXELS BRANCOS PARA PIXELS PRETOS
  for i in range(75, 1973):
    for j in range(75, 1973):
      if img[j, i] == 0:
        break
      else:
        img[j, i] = 0
    
    for j in reversed(range(75, 1973)):
      if img[j, i] == 0:
        break
      else:
        img[j, i] = 0
    
  return img

# ESTA OK
def operacoes_morfologicas_melhorada(img):
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
  img = cv2.dilate(img, kernel, iterations = 5)

  cnts = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]

  for c in cnts:
    area = cv2.contourArea(c)
    if area < 65000:
      cv2.drawContours(img, [c], -1, (0), -1)

  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(55))
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(15))

  return img
