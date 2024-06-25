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
import os
from github import Github

token = os.getenv('GITHUB_TOKEN')

print(token)

try:
    g = Github(token)
    # repo = g.get_repo("mouredev/retos-programacion-2023")
    repo = g.get_repo("JulsBetan/bt-att-contraloria-backend")

    commits = repo.get_commits()[:10]

    for i, commit in enumerate(commits):
        sha = commit.sha[:7]
        author = commit.commit.author.name
        message = commit.commit.message
        date = commit.commit.author.date.strftime("%d/%m/%Y %H:%M")
        print(f"Commit {i+1} | {sha} | {author} | {message} | {date}")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")