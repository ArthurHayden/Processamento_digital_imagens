from PIL import Image
import os

# Crie uma variável para armazenar o caminho completo da pasta
folder_path = r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02\1_C"

# Verifique se a pasta existe e crie-a, se necessário
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def reduzir_imagem(image, size):            # A função reduzir_imagem recebe a imagem e o tamanho para qual vai se reduzir
    width, height = size                    # Atribuir o tamanho da imagem que se deseja
    new_image = Image.new("L", size)        # Nova Imagem L para tons de cinza e o tamanho da imagem que se deseja 
    for x in range(width):                  # 2 for aninhados para varrer a matriz de pixeis da imagem
        for y in range(height):
            original_x = x * 512 // width   # Pega o valor do original que deve ser passado para a nova imagem
            original_y = y * 512 // height
            new_image.putpixel((x, y), image.getpixel((original_x, original_y))) # Atribui um valor do pixel da imagem
                                                                                 # original para a nova imagem
    return new_image

##PARA IMAGEM 1##

image = Image.open(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/lena_gray_512.tif")

#256x256
image_256 = reduzir_imagem(image, (256, 256))
image_256.save(os.path.join(folder_path,"image_1_256.jpg"))

image_256.show()

#128x128
image_128 = reduzir_imagem(image, (128, 128))
image_128.save(os.path.join(folder_path,"image_1_128.jpg"))
image_128.show()

#64x64
image_64 = reduzir_imagem(image, (64, 64))
image_64.save(os.path.join(folder_path,"image_1_64.jpg"))
image_64.show()

#32x32
image_32 = reduzir_imagem(image, (32, 32))
image_32.save(os.path.join(folder_path,"image_1_32.jpg"))
image_32.show()

##PARA IMAGEM 2##

image_2=Image.open(r"C:\Users\Arthur\Desktop\UNB\10_semestre_23_1\Processamento_digital_imagens\projeto_02/cameraman.tif")

#256x256
image_256 = reduzir_imagem(image_2, (256, 256))
image_256.save(os.path.join(folder_path,"image_2_256.jpg"))
image_256.show()

#128x128
image_128 = reduzir_imagem(image_2, (128, 128))
image_128.save(os.path.join(folder_path,"image_2_128.jpg"))
image_128.show()

#64x64
image_64 = reduzir_imagem(image_2, (64, 64))
image_64.save(os.path.join(folder_path,"image_2_64.jpg"))
image_64.show()

#32x32
image_32 = reduzir_imagem(image_2, (32, 32))
image_32.save(os.path.join(folder_path,"image_2_32.jpg"))
image_32.show()
