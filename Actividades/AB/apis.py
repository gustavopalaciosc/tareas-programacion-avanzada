from typing import Tuple, List
import requests
import json

from parametros import GITHUB_BASE_URL, GITHUB_REPO_OWNER, GITHUB_REPO_NAME
from parametros import GITHUB_USERNAME
from parametros import ANIME_BASE_URL, ANIME_NUMERO
from utils.anime import Anime




def get_animes() -> Tuple[int, List[Anime]]:
    # ToDo: Completar
    status_code = 404
    animes = []
    
    response = requests.get(ANIME_BASE_URL.format(f"AB?id={ANIME_NUMERO}"))
    data = response.json()
    for anime in data['animes']:
        tags = []
        nombre = anime['name']
        year = anime['season']['year']
        for n in anime['tags']:
            tags.append(n['name'])
        animes.append(Anime(nombre, year, tags))

    
    status_code = response.status_code
    

    return status_code, animes


def post_issue(token, animes: List[Anime]) -> Tuple[int, int]:
    # ToDo: Completar
    status_code = 404
    issue_number = 17
    nombres_finales = ""
    for anime in animes:
        nombres_finales += f"{anime.nombre}\n"
    header = {'Authorization': f'token {token}', 'accept': "application/vnd.github+json"}
    data = {'title': GITHUB_USERNAME, 'body': nombres_finales}
    request = requests.post(GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues"), data=json.dumps(data), headers=header)
    status_code = request.status_code



    

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404
    header = {'Authorization': f'token {token}', 'accept': "application/vnd.github+json"}
    data = {'lock_reason': 'off-topic'}

    request = requests.put(GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock"), data=json.dumps(data), headers=header)
    status_code = request.status_code


    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404
    header = {'Authorization': f'token {token}', 'accept': "application/vnd.github+json"}
    request = requests.delete(GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock"),  headers=header)
    status_code = request.status_code

    return status_code


if __name__ == "__main__":
    pass

    

