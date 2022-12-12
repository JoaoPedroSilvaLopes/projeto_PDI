from skimage.morphology import *
import copy
import cv2;

def processar_imagem(image):
  binarizada = binarização(image)
  preenchida = preenchimento_imagem(binarizada)
  subtraida = remocao_de_ruido(binarizada, preenchida)
  imagem_final = operacoes_morfologicas(subtraida)

  return (imagem_final).astype('uint8')

def binarização(img_real):
  img = copy.deepcopy(img_real)

  # ENCONTRANDO SUBÁREAS PARA ANÁLISE
  sub_img1 = img[680:820, 620:760]
  sub_img2 = img[260:400, 760:900]
  sub_img3 = img[540:680, 760:900]
  sub_img4 = img[400:540, 900:1040]
  sub_img5 = img[540:680, 1040:1180]
  sub_img6 = img[400:540, 1180:1320]

  grayScaleAreas = sorted([
    round(sub_img1.mean()), 
    round(sub_img2.mean()), 
    round(sub_img3.mean()), 
    round(sub_img4.mean()), 
    round(sub_img5.mean()), 
    round(sub_img6.mean())
  ])

  # DELETAR O ÚLTIMO E O PRIMEIRO ELEMENTO DO ARRAY
  del grayScaleAreas[5]
  del grayScaleAreas[0]

  # ENCONTRANDO O LIMIAR DA BINARIZAÇÃO
  limiar_m = round(sum(grayScaleAreas) / 4)

  # BINARIZAÇÃO
  img = cv2.threshold(img, limiar_m, 65535, cv2.THRESH_BINARY)[1]

  return img

def preenchimento_imagem(img_inicial):
  img = copy.deepcopy(img_inicial)

  # ETAPA TORNAR 50px DAS BORDAS EM PIXEIS PRETOS
  img[0:50, 0:2048] = 0
  img[0:2048, 0:50] = 0
  img[0:2048, 1998:2048] = 0
  img[1998:2048, 0:2048] = 0

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

  # # PREECHIMENTO HORIZONTAL DOS PIXELS BRANCOS PARA PIXELS PRETOS
  # for i in range(75, 1973):
  #   for j in range(75, 1973):
  #     if img[i, j] == 0:
  #       break
  #     else:
  #       img[i, j] = 0
    
  #   for j in reversed(range(75, 1973)):
  #     if img[i, j] == 0:
  #       break
  #     else:
  #       img[i, j] = 0

  return img

def remocao_de_ruido(img_inicial, img_binarizada_preenchida):
  # REMOÇÃO DE RUÍDO APÓS O PREENCHIMENTO
  ruido = cv2.subtract(img_inicial, img_binarizada_preenchida)
  
  # REALIZAÇÃO DA DILATAÇÃO COM 3 ELEMENTOS ESTRUTURANTES
  ruido = cv2.dilate(ruido, disk(60))
  ruido = cv2.dilate(ruido, rectangle(30, 10))
  ruido = cv2.dilate(ruido, rectangle(10, 30))

  # OBTENÇÃO DA IMAGEM RESULTADO PELA SUBTRAÇÃO DA IMAGEM BINARIZADA PELO RUIDO DILATADO
  ruido_dilatado = ruido

  return cv2.subtract(img_inicial, ruido_dilatado)

def operacoes_morfologicas(img):
  # REALIZAÇÃO DE OPERAÇÕES MORFOLÓGICAS DE FECHAMENTO
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, square(35))
  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(35))

  # REALIZAÇÃO DO AJUSTE DAS REGIÕES ACIMA DAS BASES PULMONARES
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], rectangle(40, 2))
  img[0:1638, 0:2048] = cv2.dilate(img[0:1638, 0:2048], octagon(17, 17))

  img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, disk(25))

  return img
