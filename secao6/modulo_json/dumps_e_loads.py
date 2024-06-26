# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null


# import json
# # from pprint import pprint
# from typing import TypedDict


# class Movie(TypedDict):
#     title: str
#     original_title: str
#     is_movie: bool
#     imdb_rating: float
#     year: int
#     characters: list[str]
#     budget: None | float


# string_json = '''
# {
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": true,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
#   "budget": null
# }
# '''
# filme: Movie = json.loads(string_json)
# # pprint(filme, width=40)
# # print(filme['title'])
# # print(filme['characters'][0])
# # print(filme['year'] + 10)

# json_string = json.dumps(filme, ensure_ascii=False, indent=2)
# print(json_string)

####################################################################

# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)