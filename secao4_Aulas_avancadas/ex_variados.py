import copy

# copy, sorted, produtos.sort
# Exercícios

# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('Lista Original')
print(*produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
print('Lista Produtos ordenados por preço')
prod_ordenados_preco = sorted(
    copy.deepcopy(produtos), key=lambda p: p['preco']
)
print(*prod_ordenados_preco, sep='\n')
print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print('Lista Ordenada por nome')
prod_ordenados_nome = sorted(
    copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True)
print(*prod_ordenados_nome, sep='\n')
print()


# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Aumente os preços dos produtos a seguir em 10%
print('Lista com 10% de aumento nos preços.')
lista_atualizada = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)]
print(*lista_atualizada, sep='\n')






