import json
import os

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

pasta = 'Orientacao_objetos'
CAMINHO = os.path.join(pasta, 'exercicio_classes.json')


class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


class Animal():
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso



# Salvando os dados da classe em json
p1 = Pessoa('Rodrigo', 'Almeida', 33)
p2 = Pessoa('Carlos', 'Alberto', 50)
p3 = Pessoa('Angelina', 'Jolie', 43)
p4 = Pessoa('Standislaw', 'Jonas', 73)

a1 = Animal('oscar', 'peixe', 0.50)
a2 = Animal('Alex', 'Leão', 2.000)


lista_pessoas = [vars(p1), vars(p2), vars(p3), vars(p4)]   
lista_animais = [a1.__dict__, a2.__dict__]

# print(lista_pessoas, sep='\n')
# print()
# print(lista_animais)

def fazer_dump():
    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(lista_pessoas, arquivo, ensure_ascii=False, indent=2)
        

if __name__ == '__main__':
    fazer_dump()