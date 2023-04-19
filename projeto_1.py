from PIL import Image, ImageDraw
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

# Define o tamanho da imagem
# cria a imagem quadrada
size = 1024
img = np.zeros((size, size), dtype=np.uint8)

# preenche a imagem com um nível de cinza constante
gray_level = 0
img.fill(gray_level)

# cria o quadrado central
square_line = 0
square = img[square_line:size-2*square_line, square_line:size-2*square_line]

# cria as listas para armazenar os valores de IL e ΔIL
IL = []
delta_IL = []
# configura a janela de exibição
cv2.namedWindow('image')
# lista para armazenar os valores de IL de cada quadrado
il_list = []
delta_il_list = []
print("digite c para criar novo quadrado\n digite + para aumentar tons de cinza\n digite - para abaixar \n digite d para ecerrar o programa\n digite g para criar os graficos ")
def on_key_press(key):
    global gray_level, square, img, square_line, size, il_list, delta_il_list, il, delta_il
    if key == ord('d'):
        # tecla 'd' para sair

        cv2.destroyAllWindows()
        sys.exit()
    elif key ==ord('g'):
        # Plot dos valores de IL
        x = np.arange(len(il_list))
        y = il_list

        # Ajuste da curva de regressão linear
        fit = np.polyfit(x, y, deg=1)
        fit_fn = np.poly1d(fit)

        # Plot dos valores de delta_IL
        x2 = np.arange(len(delta_il))
        y2 = delta_il

        # Ajuste da curva de regressão quadrática
        fit2 = np.polyfit(x2, y2, deg=2)
        fit_fn2 = np.poly1d(fit2)

        # Criação dos subplots
        fig, (ax1, ax2) = plt.subplots(2, 1)

        # Plot do gráfico de IL
        ax1.plot(x, y, 'ro', x, fit_fn(x), 'k')
        ax1.set_title('IL')
        ax1.set_xlabel('Quadrados')
        ax1.set_ylabel('Níveis de cinza')

        # Plot do gráfico de delta_IL
        ax2.plot(x2, y2, 'bo', x2, fit_fn2(x2), 'k')
        ax2.set_title('delta_IL')
        ax2.set_xlabel('Quadrados')
        ax2.set_ylabel('Variação de níveis de cinza')

        # Exibição do gráfico
        plt.show()
    elif gray_level>=255:
        print("ja esta no nivel maximo de branco gray level 255")

    elif key == ord('+'):
        # tecla '+' para aumentar o nível de cinza
        gray_level = min(gray_level + 1, 255)
        square.fill(gray_level)
    elif key == ord('-'):
        # tecla '-' para diminuir o nível de cinza
        gray_level = max(gray_level - 1, 0)
        square.fill(gray_level)
    elif key == ord('c'):
        # tecla 'c' para criar um novo quadrado interno
        square_line = square_line + 8
        square = img[square_line:size-2*square_line, square_line:size-2*square_line]
        square.fill(gray_level)
        print('Novo quadrado interno criado')
        # calcula o valor de IL do quadrado atual
        il = gray_level
        il_list.append(il)
         # verifica se a lista de valores de IL é maior que 1 (para calcular o valor de ΔIL)
   
    else:
        print('Tecla não reconhecida')
# exibe a imagem inicial
cv2.imshow('image', img)

# loop principal para lidar com as teclas do teclado
while True:
    key = cv2.waitKey(0)
    on_key_press(key)
    cv2.imshow('image', img)    

