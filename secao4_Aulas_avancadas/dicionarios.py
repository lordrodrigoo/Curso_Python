# Métodos úteis dos dicionários em Python

# len - quantas chaves
dicionario = {'nome': 'Rodrigo','idade': 33, 'altura':1.82}
print(len(dicionario))

# keys - iterável com as chaves
print(dicionario.keys())

# values - iterável com os valores
print(dicionario.values())

# items - iterável com chaves e valores
print(dicionario.items())

# setdefault - adiciona valor se a chave não existe
print(dicionario.setdefault('nome'))

# copy - retorna uma cópia rasa (shallow copy)
dicionario_2 = dicionario.copy()

# import copy  (Deep copy)
import copy
dicionario_2 = copy.deepcopy(dicionario)

# get - obtém uma chave
print(dicionario.get('nome'))

# pop - Apaga um item com a chave especificada (tipo del)
print(dicionario.pop('nome'))
print(dicionario)

# popitem - Apaga o último item adicionado
print(dicionario.popitem())
print(dicionario)

# update - Atualiza um dicionário com outro

dicionario.update({'nome': 'novo nome', 'chave': 'outra chave'})

dicionario.update(nome= 'Alberto', idade= 44, peso= 100)
print(dicionario)