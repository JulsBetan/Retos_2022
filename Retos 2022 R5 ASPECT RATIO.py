""" /*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */ """

import requests
from PIL import Image
from io import BytesIO

url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()

width, height = img.size

aspect_ratio = width / height

print(aspect_ratio)
