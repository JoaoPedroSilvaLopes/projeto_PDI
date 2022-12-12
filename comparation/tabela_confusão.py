def tabela_confusão(array_valores):
  soma = [0, 0, 0, 0]

  for valor in range(len(array_valores)):
    array_escolhido = array_valores[valor]
    for valor_array_escolhido in range(len(array_escolhido)):
      soma[valor_array_escolhido] += array_escolhido[valor_array_escolhido]

  media_valores = [round(valor / 10) for valor in soma]
  total = sum(media_valores)
  valores_tabela_confusao = [round(valor / total, 3) for valor in media_valores]

  TP = valores_tabela_confusao[0]
  FP = valores_tabela_confusao[1]
  FN = valores_tabela_confusao[2]
  TN = valores_tabela_confusao[3]

  acuracia = round((TP+TN)/(TP+TN+FP+FN), 3)
  sensibilidade = round(TP/(TP+FN), 3)
  especifidade = round(TN/(TN+FP), 3)
  F1_score = round((2*TP)/((2*TP) + FP + FN), 3)
  indice_de_jaccard = round(TP/(TP+FP+FN), 3)

  return print(
    f'TP: {TP}\nFP: {FP}\nFN: {FN}\nTN: {TN}\nAcurácia: {acuracia}\nSensibilidade: {sensibilidade}\nEspecifidade: {especifidade}\nF1 score: {F1_score}\nÍndice de jaccard: {indice_de_jaccard}\n'
  )
