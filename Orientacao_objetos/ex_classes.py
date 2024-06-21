import json
import os

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# pasta = 'Orientacao_objetos'
# CAMINHO = os.path.join(pasta, 'exercicio_classes.json')


# class Pessoa():
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade


# class Animal():
#     def __init__(self, nome, raca, peso):
#         self.nome = nome
#         self.raca = raca
#         self.peso = peso



# # Salvando os dados da classe em json
# p1 = Pessoa('Rodrigo', 'Almeida', 33)
# p2 = Pessoa('Carlos', 'Alberto', 50)
# p3 = Pessoa('Angelina', 'Jolie', 43)
# p4 = Pessoa('Standislaw', 'Jonas', 73)

# a1 = Animal('oscar', 'peixe', 0.50)
# a2 = Animal('Alex', 'Leão', 2.000)


# lista_pessoas = [vars(p1), vars(p2), vars(p3), vars(p4)]   
# lista_animais = [a1.__dict__, a2.__dict__]

# # print(lista_pessoas, sep='\n')
# # print()
# # print(lista_animais)

# def fazer_dump():
#     with open(CAMINHO, 'w', encoding='utf8') as arquivo:
#         json.dump(lista_pessoas, arquivo, ensure_ascii=False, indent=2)
        

# if __name__ == '__main__':
#     fazer_dump()


    # Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# class Carro():
    
#     def __init__(self, nome, motor, fabricante):
#         self.nome = nome
#         self.motor = motor
#         self.fabricante = fabricante
#         fabricante.adicionar_carro(self)

#     def exibir(self):
#         print(f'Carro: {self.nome}')
#         print(f'Motor: {self.motor.nome}')
#         print(f'Fabricante: {self.fabricante.nome}')

# class Motor():

#     def __init__(self, nome):
#         self.nome = nome

# class Fabricante():

#     def __init__(self, nome):
#         self.nome = nome
#         self.carros = []

#     def adicionar_carro(self, carro):
#         self.carros.append(carro)


# motor1 = Motor('V8')
# fabricante1 = Fabricante('Honda')
# carro1 = Carro('Hrv 2018', motor1, fabricante1)

# carro1.exibir()

    # Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# OUTRA FORMA 

class Carro():
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
        
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor



class Motor():
    def __init__(self, nome):
        self.nome = nome


class Fabricante():
    def __init__(self, nome):
        self.nome = nome

        
    
hrv = Carro('Hrv 2018')
honda = Fabricante('Honda')
motor_v16 = Motor('16V')

hrv.fabricante = honda
hrv.motor = motor_v16

print(hrv.nome, hrv.fabricante.nome, hrv.motor.nome)

fox = Carro('Fox 2012/2011')
volks = Fabricante('Volkswagen')
Motor_1_6 = Motor('1.6')
print('=' * 30)

fox.fabricante = volks
fox.motor = Motor_1_6
print(volks.nome, fox.nome, fox.motor.nome)
