from skimage.morphology import *
from skimage.exposure import *
from skimage.util import invert
import cv2;

# ESTA OK
def processar_imagem_melhorada(image):
  preprocessada = pre_processamento(image)
  binarizada = binarização_melhorada(preprocessada)
  preenchida = preenchimento_imagem_melhorada(binarizada)
  imagem_final = operacoes_morfologicas_melhorada(preenchida)

  return imagem_final

# ESTA OK
def filtragem(img):
  # FILTRAR USANDO CONTORNOS E REMOVENDO CONTORNOS PEQUENOS
  contornos = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  contornos = contornos[0] if len(contornos) == 2 else contornos[1]

  for contorno in contornos:
    area = cv2.contourArea(contorno)
    if area < 55000:
      cv2.drawContours(img, [contorno], -1, (0), -1)

  return img

# ESTA OK
def pre_processamento(img):
  img = (invert(rescale_intensity(img, in_range='uint12', out_range='uint16')) / 256).astype('uint8')

  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (150, 150))
  topHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
  bottomHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
  img = img + topHat - bottomHat

  img = cv2.equalizeHist(img)

  return img

# ESTA OK
def binarização_melhorada(img):
  binarizada = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  return binarizada

# ESTA OK
def preenchimento_imagem_melhorada(img):
  img = filtragem(img)
  img = cv2.morphologyEx(img, cv2.MORPH_OPEN, rectangle(30, 5))

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

  img = filtragem(img)
  img = cv2.morphologyEx(img, cv2.MORPH_OPEN, rectangle(30, 5))
  img = filtragem(img)
    
  return img

# ESTA OK
def operacoes_morfologicas_melhorada(img):
  # REALIZAÇÃO DE OPERAÇÕES MORFOLÓGICAS DE FECHAMENTO
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, square(35))
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(35))

  # REALIZAÇÃO DO AJUSTE DAS REGIÕES ACIMA DAS BASES PULMONARES
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], rectangle(40, 2))
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], octagon(17, 17))

  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(25))

  return img
