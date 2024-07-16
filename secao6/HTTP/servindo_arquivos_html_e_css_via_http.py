# python -m http.server -d secao/HTTP/aula_site/ 3333    # 3333 significa a porta

# requests para requisições HTTP

# pip install requests types-requests

import requests

# http:// -> 80
# https: // -> 443

url = 'http://localhost:3333/'

response = requests.get(url)

print(response.status_code)

# print(response.headers)

# print(response.content)  # Informará o conteudo em bytes

print(response.text)  # Informará o html