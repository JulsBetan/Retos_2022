# /*
#  * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  * 
#  */

import requests
from datetime import datetime

url = 'https://github.com/mouredev/retos-programacion-2023/commits'

token = 'token'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        commits = response.json()
        for commit in commits:
            hash_commit = commit['sha']
            # author = commit['commit']['author']['name']
            # message = commit['commit']['message']
            # date = commit['commit']['author']['date']
            # formatted_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

            print(f"Hash: {hash_commit}")
            # print(f"Author: {author}")
            # print(f"Message: {message}")
            # print(f"Date: {formatted_date}")
            # print("-" * 40)
    except ValueError as e:
        print("Error al decodificar la respuesta JSON:", e)
        print("Respuesta no válida:", response.text[:1000])
else:
    print(f"Error: Unable to fetch commits (Status Code: {response.status_code})")
    print("Response Headers:", response.headers)
    print("Response Text:", response.text)
