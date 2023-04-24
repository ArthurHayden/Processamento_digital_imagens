import cv2
import numpy as np

def quantize_image(img, n_bits):
    n_levels = 2 ** n_bits
    quantization_rate = 256 / n_levels
    img = (np.round(img / quantization_rate) * quantization_rate).astype(np.uint8)
    return img

## PARA IMAGEM 1 ##
img = cv2.imread(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/lena_gray_512.tif", cv2.IMREAD_GRAYSCALE)

# 7 bits
img_7bits = quantize_image(img, 7)
cv2.imwrite("image_1_7bits.jpg", img_7bits)

# 6 bits
img_6bits = quantize_image(img, 6)
cv2.imwrite("image_1_6bits.jpg", img_6bits)

# 5 bits
img_5bits = quantize_image(img, 5)
cv2.imwrite("image_1_5bits.jpg", img_5bits)

# 4 bits
img_4bits = quantize_image(img, 4)
cv2.imwrite("image_1_4bits.jpg", img_4bits)

# 3 bits
img_3bits = quantize_image(img, 3)
cv2.imwrite("image_1_3bits.jpg", img_3bits)

# 2 bits
img_2bits = quantize_image(img, 2)
cv2.imwrite("image_1_2bits.jpg", img_2bits)

# 1 bits
img_1bit = quantize_image(img, 1)
cv2.imwrite("image_1_1bit.jpg", img_1bit)

# PARA IMAGEM 2 ##

img_2 = cv2.imread(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/Fig0219(rose1024).tif", cv2.IMREAD_GRAYSCALE)

# 7 bits
img_2_7bits = quantize_image(img_2, 7)
cv2.imwrite("image_2_7bits.jpg", img_2_7bits)

# 6 bits
img_2_6bits = quantize_image(img_2, 6)
cv2.imwrite("image_2_6bits.jpg", img_2_6bits)

# 5 bits
img_2_5bits = quantize_image(img_2, 5)
cv2.imwrite("image_2_5bits.jpg", img_2_5bits)

# 4 bits
img_2_4bits = quantize_image(img_2, 4)
cv2.imwrite("image_2_4bits.jpg", img_2_4bits)

# 3 bits
img_2_3bits = quantize_image(img_2, 3)
cv2.imwrite("image_2_3bits.jpg", img_2_3bits)

# 2 bits
img_2_2bits = quantize_image(img_2, 2)
cv2.imwrite("image_2_2bits.jpg", img_2_2bits)

# 1 bits
img_2_1bit = quantize_image(img_2, 1)
cv2.imwrite("image_2_1bit.jpg", img_2_1bit)

## PARA IMAGEM 3 ##

img_3 = cv2.imread(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/walkbridge.tif", cv2.IMREAD_GRAYSCALE) 

# 7 bits
img_3_7bits = quantize_image(img_3, 7)
cv2.imwrite("image_3_7bits.jpg", img_3_7bits)

# 6 bits
img_3_6bits = quantize_image(img_3, 6)
cv2.imwrite("image_3_6bits.jpg", img_3_6bits)

# 5 bits
img_3_5bits = quantize_image(img_3, 5)
cv2.imwrite("image_3_5bits.jpg", img_3_5bits)

# 4 bits
img_3_4bits = quantize_image(img_3, 4)
cv2.imwrite("image_3_4bits.jpg", img_3_4bits)

# 3 bits
img_3_3bits = quantize_image(img_3, 3)
cv2.imwrite("image_3_3bits.jpg", img_3_3bits)

# 2 bits
img_3_2bits = quantize_image(img_3, 2)
cv2.imwrite("image_3_2bits.jpg", img_3_2bits)

# 1 bits
img_3_1bit = quantize_image(img_3, 1)
cv2.imwrite("image_3_1bit.jpg", img_3_1bit)