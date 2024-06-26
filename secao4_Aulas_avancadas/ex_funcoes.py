# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicar(*args):
    tot = 1
    for numero in args:
        tot *= numero
    return print(f'O total da multiplicação é = {tot}')


multiplicar(5, 5)
multiplicar(2, 10)
multiplicar(5 , 4, 3, 2, 1)
multiplicar(100, 100)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return print(f'O número {numero} é pár!')
    return print(f'O número {numero} é ímpar!')

par_impar(2)
par_impar(3)
par_impar(5)
par_impar(10)

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

