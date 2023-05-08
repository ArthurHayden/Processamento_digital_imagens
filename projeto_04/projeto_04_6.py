import cv2
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definição das variáveis fuzzy de entrada e saída
pixel_original = ctrl.Antecedent(np.arange(0, 256), 'pixel_original')
pixel_saida = ctrl.Consequent(np.arange(0, 256), 'pixel_saida')

# Definição das funções de pertinência para a variável de entrada
pixel_original['escuro'] = fuzz.trimf(pixel_original.universe, [0, 0, 127])
pixel_original['cinza'] = fuzz.trimf(pixel_original.universe, [64, 127, 191])
pixel_original['claro'] = fuzz.trimf(pixel_original.universe, [128, 255, 255])

# Definição das funções de pertinência para a variável de saída
pixel_saida['mais_escuro'] = fuzz.trimf(pixel_saida.universe, [0, 120, 140])
pixel_saida['cinza'] = fuzz.trimf(pixel_saida.universe, [50, 127, 180])
pixel_saida['mais_claro'] = fuzz.trimf(pixel_saida.universe, [180, 255, 255])

# Definição das regras de inferência
regra1 = ctrl.Rule(pixel_original['escuro'], pixel_saida['mais_escuro'])
regra2 = ctrl.Rule(pixel_original['cinza'], pixel_saida['cinza'])
regra3 = ctrl.Rule(pixel_original['claro'], pixel_saida['mais_claro'])

# Criação do sistema de controle fuzzy
sistema_fuzzy = ctrl.ControlSystem([regra1, regra2, regra3])

# Criação da simulação do sistema de controle
simulacao = ctrl.ControlSystemSimulation(sistema_fuzzy)

# Carregamento da imagem de entrada
imagem = cv2.imread(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/flores.tif", cv2.IMREAD_GRAYSCALE)

# Aplicação do algoritmo de realce fuzzy na imagem
imagem_saida = np.zeros(imagem.shape, np.uint8)
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        pixel = int(imagem[i,j])
        simulacao.input['pixel_original'] = pixel
        simulacao.compute()
        pixel_saida = int(round(simulacao.output['pixel_saida']))
        imagem_saida[i,j] = pixel_saida
        
# Comparação entre as imagens original e realçada
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 5))

ax0.imshow(imagem, cmap='gray')
ax0.set_title('Imagem Original')

ax1.imshow(imagem_saida, cmap='gray')
ax1.set_title('Imagem Realçada')

plt.show()
