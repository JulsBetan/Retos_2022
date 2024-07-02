# *
#  * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#  * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#  *
#  * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#  * del día 8. Mostrando hora e información de cada uno.
#  * Ejemplo: "16:00 | Bienvenida"
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  *
#  */

import requests
from bs4 import BeautifulSoup 

url  = 'https://holamundo.day'

response = requests.get(url)

if response.status_code == 200:
    page_content = response.content

    soup = BeautifulSoup(page_content, 'html.parser')

    print('Encabezados:')
    for header in soup.find_all(['h1','h2','h3','h4','h5','h6']):
        print(header.text.strip())

    print("\nURLs:")
    for link in soup.find_all('a', href=True):
        print(link['href'])

    print('\nAgenda:')
    
    #agenda_block = soup.find('Agenda')
    
    h2_elements = soup.find_all('h2')

# Busca el elemento h2 que contenga el texto "Agenda"
    agenda_heading = None
    for h2 in h2_elements:
        if 'Agenda' in h2.get_text():
            agenda_heading = h2
            break
    # print(agenda_heading)

    if agenda_heading:
    # Encuentra el div padre que contiene el h2
        parent_div = agenda_heading.find_parent('div', class_='rt-Flex')

        if parent_div:
            # Encuentra el div superior al actual (el div padre del parent_div)
            div_container = parent_div.find_parent('div', class_='rt-Flex')

            if div_container:
                # Imprime el contenido del div superior
                # print(div_container.prettify())

                # Encuentra todos los elementos span dentro del div
                agenda_items = div_container.find_all('span', class_='rt-Text rt-r-size-4')

                # Extrae los textos de los elementos de la agenda
                for item in agenda_items:
                    time = item.find('strong', class_='rt-Strong css-ksqtdq').get_text(strip=True)
                    description = item.get_text(strip=True).replace(time, '').strip()
                    print(f"{time} - {description}")
            else:
                print("No se encontró el div contenedor superior.")
        else:
            print("No se encontró el div padre.")
    else:
        print("No se encontró la sección de Agenda.")  
else:
    print(f'Error: {response.status_code}')


blockquotes = BeautifulSoup(requests.get(
    "https://holamundo.day").content, 'html.parser').find_all("blockquote")

print(blockquotes)
for blockquote in blockquotes[21:]:
    print(blockquote.text)