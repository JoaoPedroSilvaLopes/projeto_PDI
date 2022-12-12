from tabela_confusão import *
import cv2;

# ARRAY DAS IMAGENS
image_array = [
  'JPCNN001',
  'JPCNN003',
  'JPCNN005',
  'JPCNN006',
  'JPCNN008',
  'JPCNN009',
  'JPCNN010',
  'JPCLN006',
  'JPCLN008',
  'JPCLN009'
]

final_array_original = []
final_array_melhoria = []

# ESTA COMENTADO, POIS PARA FAZER A VARREDURA PIXEL A PIXEL É MUITO CUSTOSO
# RESULTADO PRÉVIO JÁ ESTA EM BAIXO

# for image_name in image_array:
#   #if image_name == 'JPCNN003':
#   array_comparacoes_original = [0, 0, 0, 0]
#   array_comparacoes_melhoria = [0, 0, 0, 0]

#   teste1 = []
#   teste2 = []
#   teste3 = []

#   # CARREGAMENTO DOS GROUND_TRUTH
#   ground_truth_image = cv2.imread(f'ground_truths/{image_name}GT.bmp', cv2.IMREAD_GRAYSCALE)
#   ground_truth_image = cv2.threshold(ground_truth_image, 127, 255, cv2.THRESH_BINARY)[1]

#   # CARREGAR IMAGENS A SEREM COMPARADAS
#   result_image_original_method = cv2.imread(f'comparation/images_result_original_method/{image_name}.png', cv2.IMREAD_GRAYSCALE)
#   result_image_proposed_method = cv2.imread(f'comparation/images_result_proposed_method/{image_name}.png', cv2.IMREAD_GRAYSCALE)

#   for linha in ground_truth_image:
#     for coluna in linha:
#       teste1.append(coluna)

#   for linha in result_image_original_method:
#     for coluna in linha:
#       teste2.append(coluna)

#   for linha in result_image_proposed_method:
#     for coluna in linha:
#       teste3.append(coluna)

#   for valor in range(len(teste1)):
#     if teste1[valor] == 255 and teste2[valor] == 255:
#         array_comparacoes_original[0] += 1

#     elif teste1[valor] == 255 and teste2[valor] == 0:
#         array_comparacoes_original[1] += 1

#     elif teste1[valor] == 0 and teste2[valor] == 255:
#         array_comparacoes_original[2] += 1

#     else:
#         array_comparacoes_original[3] += 1

#     # =================================================

#     if teste1[valor] == 255 and teste3[valor] == 255:
#         array_comparacoes_melhoria[0] += 1

#     elif teste1[valor] == 255 and teste3[valor] == 0:
#         array_comparacoes_melhoria[1] += 1

#     elif teste1[valor] == 0 and teste3[valor] == 255:
#         array_comparacoes_melhoria[2] += 1

#     else:
#         array_comparacoes_melhoria[3] += 1

#   final_array_original.append(array_comparacoes_original)
#   final_array_melhoria.append(array_comparacoes_melhoria)

final_array_original = [[1373559, 208113, 97833, 2514799], [421433, 553638, 89890, 3129343], [1371208, 236519, 124206, 2462371], [1149408, 199114, 78999, 2766783], [1172268, 278499, 72289, 2671248], [1212207, 122694, 103764, 2755639], [1361349, 143517, 105418, 2584020], [894198, 315795, 45816, 2938495], [1479899, 169975, 75263, 2469167], [580280, 671216, 57823, 2884985]]
final_array_melhoria = [[1501971, 79701, 205571, 2407061], [929490, 45581, 244843, 2974390], [1502355, 105372, 255833, 2330744], [1303423, 45099, 205022, 2640760], [1408717, 42050, 222836, 2520701], [1263953, 70948, 142369, 2717034], [1418341, 86525, 150967, 2538471], [1084169, 125824, 122257, 2862054], [1431157, 218717, 79078, 2465352], [1127215, 124281, 336989, 2605819]]

tabela_confusão(final_array_original)
tabela_confusão(final_array_melhoria)
