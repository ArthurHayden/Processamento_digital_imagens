######################################### HISTOGRAMA,PDF E CDF ############################################################

####################Einstein
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem em escala de cinza
img_einstein = plt.imread(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/einstein.tif")


# Calculando o histograma da imagem
hist, bins = np.histogram(img_einstein.flatten(), 256, [0,256])

# Calculando o histograma normalizado (PDF)
pdf = hist / float(np.sum(hist))

# Calculando a função de massa de probabilidade acumulada (CDF)
cdf = np.cumsum(pdf)

# Plotando o histograma, o PDF e o CDF
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

ax1.hist(img_einstein.flatten(), 256, [0,256])
ax1.set_title("Histograma einstein")
ax1.set_xlabel("Intensidade")
ax1.set_ylabel("Frequência")

ax2.plot(pdf)
ax2.set_title("Histograma normalizado (PDF)")
ax2.set_xlabel("Intensidade")
ax2.set_ylabel("Probabilidade")

ax3.plot(cdf)
ax3.set_title("Função massa de probabilidade acumulada  (CDF)")
ax3.set_xlabel("Intensidade")
ax3.set_ylabel("Probabilidade acumulada")

plt.show()
#############Flores
# Carregando a imagem em escala de cinza
img_flores = plt.imread(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/flores.tif")


# Calculando o histograma da imagem
hist, bins = np.histogram(img_flores.flatten(), 256, [0,256])

# Calculando o histograma normalizado (PDF)
pdf = hist / float(np.sum(hist))

# Calculando a função de massa de probabilidade acumulada (CDF)
cdf = np.cumsum(pdf)

# Plotando o histograma, o PDF e o CDF
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

ax1.hist(img_flores.flatten(), 256, [0,256])
ax1.set_title("Histograma flores")
ax1.set_xlabel("Intensidade")
ax1.set_ylabel("Frequência")

ax2.plot(pdf)
ax2.set_title("Histograma normalizado (PDF)")
ax2.set_xlabel("Intensidade")
ax2.set_ylabel("Probabilidade")

ax3.plot(cdf)
ax3.set_title("Função massa de probabilidade acumulada  (CDF)")
ax3.set_xlabel("Intensidade")
ax3.set_ylabel("Probabilidade acumulada")

plt.show()
###################pollen

# Carregando a imagem em escala de cinza
img_pollen = plt.imread(r"C:/Users/Arthur/Desktop/UNB/10_semestre_23_1/Processamento_digital_imagens/projeto_04/pollen.tif")


# Calculando o histograma da imagem
hist, bins = np.histogram(img_pollen.flatten(), 256, [0,256])

# Calculando o histograma normalizado (PDF)
pdf = hist / float(np.sum(hist))

# Calculando a função de massa de probabilidade acumulada (CDF)
cdf = np.cumsum(pdf)

# Plotando o histograma, o PDF e o CDF
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

ax1.hist(img_einstein.flatten(), 256, [0,256])
ax1.set_title("Histograma pollen")
ax1.set_xlabel("Intensidade")
ax1.set_ylabel("Frequência")

ax2.plot(pdf)
ax2.set_title("Histograma normalizado (PDF)")
ax2.set_xlabel("Intensidade")
ax2.set_ylabel("Probabilidade")

ax3.plot(cdf)
ax3.set_title("Função massa de probabilidade acumulada  (CDF)")
ax3.set_xlabel("Intensidade")
ax3.set_ylabel("Probabilidade acumulada")

plt.show()