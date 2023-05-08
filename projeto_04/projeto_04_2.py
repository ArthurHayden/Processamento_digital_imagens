#################################### ALARGAMENTO DE CONTRASTE COM SIGMOIDE ################################################
import numpy as np
import matplotlib.pyplot as plt
def sigmoidal_contrast(img, a):
    # Calculando o histograma e a cdf da imagem
    hist, bins = np.histogram(img.ravel(), 256, [0,256])
    cdf_Img = hist.cumsum()
    
    # Recortando a cdf_Img e bins para excluir os extremos
    idx = (cdf_Img > 0) & (cdf_Img < cdf_Img.max())
    cdf_up = cdf_Img[idx]
    bins = bins[1:][idx]
  
    # Calculando a regressão linear dos pontos da cdf que excluem os extremos
    slope, intercept = np.polyfit(bins, cdf_up, 1)
    cdf_up_lin = slope * bins + intercept
    
    # Calculando o ponto de inflexão m da função sigmoide
    m = (bins[cdf_up_lin.argmax()] + bins[cdf_up_lin.argmin()]) / 2
    
    # Calculando a função sigmoide de contraste
    sigm = 1 / (1 + np.exp(-a*(bins - m)))
    
    # Normalizando a função sigmoide para que o mínimo seja 0 e o máximo seja 1
    sigm_norm = (sigm - sigm.min()) / (sigm.max() - sigm.min())
    
    # Aplicando a função de contraste na imagem
    img_contrast = np.interp(img, bins, sigm_norm * 255)
    
    return img_contrast.astype('uint8')

# Valores de teste de a
a_val = [0.8, 0.1, 0.01]
img_einstein = plt.imread(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/einstein.tif")
# Plotar a imagem contrastada
for a in a_val:
    img_contrast_einstein = sigmoidal_contrast(img_einstein, a)
    # Plotando as imagens
    plt.figure()
    plt.subplot(121)
    plt.imshow(img_einstein, cmap="gray")
    plt.title("Imagem original")
    plt.subplot(122)
    plt.imshow(img_contrast_einstein, cmap="gray")
    plt.title("Imagem com contraste alargado (a = {})".format(a))
    plt.show()
    #Plotando Histograma da imagem
    hist, bins = np.histogram(img_contrast_einstein.flatten(), 256, [0,256])
    plt.hist(img_contrast_einstein.flatten(), 256, [0,256])
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")