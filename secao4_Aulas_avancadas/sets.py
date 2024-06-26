# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# add
s1 = set()
s1.add('Rodrigo')

# update
s1.update(('Algo a mais','mais um texto'))
print(s1)

# clear  -> Limpa o conjunto
s1.clear()

# discard  -> Elimina um valor selecionado
s1.discard('Algo a mais')
print(s1)


# Operadores úteis:
# união | união (union) - Une

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1 | set2
print(set3)


# intersecção & (intersection) - Itens presentes em ambos
set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1 & set2
print(set3)


# diferença - Itens presentes apenas no set da esquerda

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1 - set2
print(set3)

# diferença simétrica ^ - Itens que não estão em ambos

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1 ^ set2
print(set3)

