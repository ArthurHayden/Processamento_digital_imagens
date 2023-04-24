
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from PIL.Image import Resampling
import os
folder_path = r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02\1_C"

# Verifique se a pasta existe e crie-a, se necessário
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Função para redimensionar a imagem
def resize_image(image, size):
    # Crie uma nova imagem do tamanho especificado com interpolação bilinear
    width, height = size 
    new_image = Image.new("RGB", (width, height), (255, 255, 255))
    # Calcule a proporção de escalonamento em cada dimensão
    scale_x = image.size[0] / size[0]
    scale_y = image.size[1] / size[1]

    # Para cada pixel na nova imagem, encontre o pixel correspondente na imagem original
    for y in range(size[1]):
        for x in range(size[0]):
            # Encontre as coordenadas do pixel correspondente na imagem original
            orig_x = round(x * scale_x)
            orig_y = round(y * scale_y)

            # Verifique se as coordenadas estão dentro dos limites da imagem original
            if orig_x >= image.size[0]:
                orig_x = image.size[0] - 1
            if orig_y >= image.size[1]:
                orig_y = image.size[1] - 1

            # Obtenha o valor do pixel correspondente na imagem original
            pixel_value = image.getpixel((orig_x, orig_y))

            # Atribua o valor do pixel na nova imagem
            new_image.putpixel((x, y), pixel_value)

    return new_image

# Tamanhos de imagem a serem redimensionados
sizes = [32, 64, 128, 256]

# Abra cada imagem, redimensione e salve
for size in sizes:
    #imagem 1
    image_path = os.path.join(folder_path, f"image_1_{size}.jpg")
    image = Image.open(image_path)
    image = ImageOps.grayscale(image)

    #imagem 2
    image2_path = os.path.join(folder_path, f"image_2_{size}.jpg")
    image2 = Image.open(image2_path)
    image2 = ImageOps.grayscale(image2)


    new_size = (512, 512)

    resized_image = resize_image(image, new_size)
    resized_image= ImageOps.grayscale(resized_image)
    #imagem 2
    resized2_image = resize_image(image2, new_size)
    resized2_image= ImageOps.grayscale(resized2_image)


    # Salve a imagem redimensionada
    resized_image.save(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02\2_D\image_1_{}_r_b.jpg".format(size))
    #para imagem 2
    resized2_image.save(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02\2_D\image_2_{}_r_b.jpg".format(size))
