########################################## EQUALIZAÇÃO DE HISTOGRAMA #####################################################
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def histogram(img):
    """Calcula o histograma da imagem."""
    h = np.zeros(256)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            h[img[i,j]] += 1
    return h

def cdf(h):
    """Calcula a função de distribuição acumulada (CDF) do histograma."""
    c = np.zeros(256)
    c[0] = h[0]
    for i in range(1, 256):
        c[i] = c[i-1] + h[i]
    return c

def equalize(img):
    """Equaliza o histograma da imagem."""
    # Calcula o histograma e a CDF da imagem
    h = histogram(img)
    c = cdf(h)
    # Normaliza a CDF para mapear os valores de intensidade para [0, 255]
    c_norm = c / (img.shape[0] * img.shape[1])
    c_norm *= 255
    # Aplica a transformação de intensidade
    img_eq = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_eq[i,j] = round(c_norm[img[i,j]])
    return img_eq

# Carrega a imagem 1 e converte para tons de cinza
img = np.array(Image.open(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/einstein.tif").convert('L'))

# Equaliza o histograma da imagem
img_eq = equalize(img)

# Plota o histograma e a imagem original e a equalizada
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem original')
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma original')
plt.subplot(2, 2, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Imagem equalizada')
plt.subplot(2, 2, 4)
plt.hist(img_eq.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma equalizado')
plt.show()

# Carregar Imagem 2
img = np.array(Image.open(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/pollen.tif").convert('L'))
# Equaliza o histograma da imagem
img_eq = equalize(img)

# Plota o histograma e a imagem original e a equalizada
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem original')
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma original')
plt.subplot(2, 2, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Imagem equalizada')
plt.subplot(2, 2, 4)
plt.hist(img_eq.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma equalizado')
plt.show()

# Carregar imagem 3
img = np.array(Image.open(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/flores.tif").convert('L'))

# Equaliza o histograma da imagem
img_eq = equalize(img)

# Plota o histograma e a imagem original e a equalizada
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagem original')
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma original')
plt.subplot(2, 2, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Imagem equalizada')
plt.subplot(2, 2, 4)
plt.hist(img_eq.ravel(), bins=256, range=(0, 255), color='k')
plt.title('Histograma equalizado')
plt.show()