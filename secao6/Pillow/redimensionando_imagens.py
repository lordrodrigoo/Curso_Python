# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'Bolo de Cenoura com cobertura de chocolate.jpg'

NEW_IMAGE = ROOT_FOLDER / 'new.jpg'


pil_image = Image.open(ORIGINAL)

width, height = pil_image.size

#exif = pil_image.info['exif']  # Serve para fornecer dados da imagem
# Modelo da camera etc.. nem todas as fotos possui informações.

print(pil_image.size)

# width         new_width
# height        new_height

new_width = 360
new_height = 360

new_image = pil_image.resize((new_width, new_height))
new_image.save(NEW_IMAGE, optimize=True,  quality=70)