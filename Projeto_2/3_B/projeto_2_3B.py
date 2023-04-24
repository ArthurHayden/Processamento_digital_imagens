import numpy as np
from PIL import Image
import cv2

def reduzir_imagem(image, size):            
    width, height = size                    
    new_image = Image.new("L", size)        
    for x in range(width):                  
        for y in range(height):
            original_x = x * 512 // width   
            original_y = y * 512 // height
            new_image.putpixel((x, y), image.getpixel((original_x, original_y)))                                                                         
    return new_image

def quantize_image(img, n_bits):
    img_np = np.array(img)
    n_levels = 2 ** n_bits
    quantization_rate = 256 / n_levels
    img_np = (np.round(img_np / quantization_rate) * quantization_rate).astype(np.uint8)
    img = Image.fromarray(img_np)
    return img

## Para Imagem 1 ##
image = Image.open(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/lena_gray_512.tif")

#256x256
image_256 = reduzir_imagem(image, (256, 256))
image_256.save("image_1_256.jpg")

#128x128
image_128 = reduzir_imagem(image, (128, 128))
image_128.save("image_1_128.jpg")

#64x64
image_64 = reduzir_imagem(image, (64, 64))
image_64.save("image_1_64.jpg")

#32x32
image_32 = reduzir_imagem(image, (32, 32))
image_32.save("image_1_32.jpg")

# Image quantize 256x256
image_256_6 = quantize_image(image_256 , 6)
image_256_6.save("image_1_256_6.jpg")
image_256_5 = quantize_image(image_256 , 5)
image_256_5.save("image_1_256_5.jpg")
image_256_4 = quantize_image(image_256 , 4)
image_256_4.save("image_1_256_4.jpg")
image_256_3 = quantize_image(image_256 , 3)
image_256_3.save("image_1_256_3.jpg")

# Image quantize 128x128
image_128_6 = quantize_image(image_128 , 6)
image_128_6.save("image_1_128_6.jpg")
image_128_5 = quantize_image(image_128 , 5)
image_128_5.save("image_1_128_5.jpg")
image_128_4 = quantize_image(image_128 , 4)
image_128_4.save("image_1_128_4.jpg")
image_128_3 = quantize_image(image_128 , 3)
image_128_3.save("image_1_128_3.jpg")

# Image quantize 64x64
image_64_6 = quantize_image(image_64 , 6)
image_64_6.save("image_1_64_6.jpg")
image_64_5 = quantize_image(image_64 , 5)
image_64_5.save("image_1_64_5.jpg")
image_64_4 = quantize_image(image_64 , 4)
image_64_4.save("image_1_64_4.jpg")
image_64_3 = quantize_image(image_64 , 3)
image_64_3.save("image_1_64_3.jpg")

# Image quantize 32x32
image_32_6 = quantize_image(image_32 , 6)
image_32_6.save("image_1_32_6.jpg")
image_32_5 = quantize_image(image_32 , 5)
image_32_5.save("image_1_32_5.jpg")
image_32_4 = quantize_image(image_32 , 4)
image_32_4.save("image_1_32_4.jpg")
image_32_3 = quantize_image(image_32 , 3)
image_32_3.save("image_1_32_3.jpg")

## Para a Imagem 2 ##
image_2 = Image.open(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/Fig0219(rose1024).tif")

#256x256
image_2_256 = reduzir_imagem(image_2, (256, 256))
image_2_256.save("image_2_256.jpg")

#128x128
image_2_128 = reduzir_imagem(image_2, (128, 128))
image_2_128.save("image_2_128.jpg")

#64x64
image_2_64 = reduzir_imagem(image_2, (64, 64))
image_2_64.save("image_2_64.jpg")

#32x32
image_2_32 = reduzir_imagem(image_2, (32, 32))
image_2_32.save("image_2_32.jpg")

# Image quantize 256x256
image_2_256_6 = quantize_image(image_2_256 , 6)
image_2_256_6.save("image_2_256_6.jpg")
image_2_256_5 = quantize_image(image_2_256 , 5)
image_2_256_5.save("image_2_256_5.jpg")
image_2_256_4 = quantize_image(image_2_256 , 4)
image_2_256_4.save("image_2_256_4.jpg")
image_2_256_3 = quantize_image(image_2_256 , 3)
image_2_256_3.save("image_2_256_3.jpg")

# Image quantize 128x128
image_2_128_6 = quantize_image(image_2_128 , 6)
image_2_128_6.save("image_2_128_6.jpg")
image_2_128_5 = quantize_image(image_2_128 , 5)
image_2_128_5.save("image_2_128_5.jpg")
image_2_128_4 = quantize_image(image_2_128 , 4)
image_2_128_4.save("image_2_128_4.jpg")
image_2_128_3 = quantize_image(image_2_128 , 3)
image_2_128_3.save("image_2_128_3.jpg")

# Image quantize 64x64
image_2_64_6 = quantize_image(image_2_64 , 6)
image_2_64_6.save("image_2_64_6.jpg")
image_2_64_5 = quantize_image(image_2_64 , 5)
image_2_64_5.save("image_2_64_5.jpg")
image_2_64_4 = quantize_image(image_2_64 , 4)
image_2_64_4.save("image_2_64_4.jpg")
image_2_64_3 = quantize_image(image_2_64 , 3)
image_2_64_3.save("image_2_64_3.jpg")

# Image quantize 32x32
image_2_32_6 = quantize_image(image_2_32 , 6)
image_2_32_6.save("image_2_32_6.jpg")
image_2_32_5 = quantize_image(image_2_32 , 5)
image_2_32_5.save("image_2_32_5.jpg")
image_2_32_4 = quantize_image(image_2_32 , 4)
image_2_32_4.save("image_2_32_4.jpg")
image_2_32_3 = quantize_image(image_2_32 , 3)
image_2_32_3.save("image_2_32_3.jpg")

## Para a Imagem 3 ##
image_3 = Image.open(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/walkbridge.tif")

#256x256
image_3_256 = reduzir_imagem(image_3, (256, 256))
image_3_256.save("image_3_256.jpg")

#128x128
image_3_128 = reduzir_imagem(image_3, (128, 128))
image_3_128.save("image_3_128.jpg")

#64x64
image_3_64 = reduzir_imagem(image_3, (64, 64))
image_3_64.save("image_3_64.jpg")

#32x32
image_3_32 = reduzir_imagem(image_3, (32, 32))
image_3_32.save("image_3_32.jpg")

# Image quantize 256x256
image_3_256_6 = quantize_image(image_3_256 , 6)
image_3_256_6.save("image_3_256_6.jpg")
image_3_256_5 = quantize_image(image_3_256 , 5)
image_3_256_5.save("image_3_256_5.jpg")
image_3_256_4 = quantize_image(image_3_256 , 4)
image_3_256_4.save("image_3_256_4.jpg")
image_3_256_3 = quantize_image(image_3_256 , 3)
image_3_256_3.save("image_3_256_3.jpg")

# Image quantize 128x128
image_3_128_6 = quantize_image(image_3_128 , 6)
image_3_128_6.save("image_3_128_6.jpg")
image_3_128_5 = quantize_image(image_3_128 , 5)
image_3_128_5.save("image_3_128_5.jpg")
image_3_128_4 = quantize_image(image_3_128 , 4)
image_3_128_4.save("image_3_128_4.jpg")
image_3_128_3 = quantize_image(image_3_128 , 3)
image_3_128_3.save("image_3_128_3.jpg")

# Image quantize 64x64
image_3_64_6 = quantize_image(image_3_64 , 6)
image_3_64_6.save("image_3_64_6.jpg")
image_3_64_5 = quantize_image(image_3_64 , 5)
image_3_64_5.save("image_3_64_5.jpg")
image_3_64_4 = quantize_image(image_3_64 , 4)
image_3_64_4.save("image_3_64_4.jpg")
image_3_64_3 = quantize_image(image_3_64 , 3)
image_3_64_3.save("image_3_64_3.jpg")

# Image quantize 32x32
image_3_32_6 = quantize_image(image_3_32 , 6)
image_3_32_6.save("image_3_32_6.jpg")
image_3_32_5 = quantize_image(image_3_32 , 5)
image_3_32_5.save("image_3_32_5.jpg")
image_3_32_4 = quantize_image(image_3_32 , 4)
image_3_32_4.save("image_3_32_4.jpg")
image_3_32_3 = quantize_image(image_3_32 , 3)
image_3_32_3.save("image_3_32_3.jpg")