import pandas as pd

data = pd.read_csv('../datasets/classification_results_trial_0001.csv')
data

data['real_class'].value_counts()

imagens_com_erro = data.loc[data['real_class'] != data['predicted_class'], 'image_path']

print(imagens_com_erro)

import numpy as np

data['confianca'] = np.where(data['predicted_class'] == 'malign', 
                             data['prob_malign'], 
                             data['prob_benign'])

erros_confiantes = data[data['real_class'] != data['predicted_class']].sort_values(by='confianca', ascending=False)

print(erros_confiantes[['image_path', 'confianca']])

# a. TP (Verdadeiro Positivo): Era maligno e o modelo acertou
tp = len(data[(data['real_class'] == 'malign') & (data['predicted_class'] == 'malign')])

# b. TN (Verdadeiro Negativo): Era benigno e o modelo acertou
tn = len(data[(data['real_class'] == 'benign') & (data['predicted_class'] == 'benign')])

# c. FP (Falso Positivo): Era benigno, mas o modelo disse que era maligno (Alarme Falso)
fp = len(data[(data['real_class'] == 'benign') & (data['predicted_class'] == 'malign')])

# d. FN (Falso Negativo): Era maligno, mas o modelo disse que era benigno (Erro Crítico)
fn = len(data[(data['real_class'] == 'malign') & (data['predicted_class'] == 'benign')])

print(f"TP: {tp} | TN: {tn} | FP: {fp} | FN: {fn}")

# a. Acurácia: (TP+TN)/(TP+TN+FP+FN)
acuracia = (tp + tn) / (tp + tn + fp + fn)

#b. Precisão: TP/(TP+FP)
precisao = tp / (tp + fp)

#c. Recall: TP/(TP+FN)
recall = tp / (tp + fn)

#d. Especificidade: TN/(TN+FP)
especif = tn / (tn + fp)

print(f"Acuracia: {acuracia:.3f} | Precisao: {precisao:.3f} | Recall: {recall:.3f} | Especificidade: {especif:.3f}")

# Filtra apenas as imagens que são realmente benignas
benign_criticas = data[data['real_class'] == 'benign']

# Ordena pela menor probabilidade de ser benigno
top5_duvidosas = benign_criticas.sort_values(by='prob_benign').head(5)

print(top5_duvidosas[['image_path', 'real_class', 'predicted_class', 'prob_benign']])

# Filtra apenas as imagens que são realmente malignas
malign_criticas = data[data['real_class'] == 'malign']

# Ordena pela menor probabilidade de ser maligno
top5_falsos_negativos = malign_criticas.sort_values(by='prob_malign').head(5)

print(top5_falsos_negativos[['image_path', 'real_class', 'predicted_class', 'prob_malign']])