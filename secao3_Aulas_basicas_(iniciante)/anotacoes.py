# qualquer coisa
# Sobre prints


print(12, 34, sep= ' ')   # -> Com o sep=  você pode escolher qual separador você quer usar.

print('alguma coisa', end='\n')  # -> O end= significa quebra de linha 



# Tipos de dados.

# Escape
print("rodrigo \"almeida\"")  # -> \" " Mostra o segundo nome com aspas

# Mais simples
print('rodrigo '"almeida")

# Conversão de tipos (coerção)

"""
Existem varios nomes para conversão de tipos:
    - typecasting
    - coercion
    - type convertion

É o ato de converter um tipo em outro
"""

x = int(12)

x = str(x)

print(type(x))


"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condicao = True

if condicao:
    print('Faça algo')
else:
    print('Não faça algo')


"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = input('Informe um número inteiro: ')
    if int(num) % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é ímpar!')    
except ValueError:
    print(f'"{num}" não é um número inteiro!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horas = float(input('Que horas são? '))

if 6 >= horas < 12:
    print('Bom dia!')
elif 12 <= horas < 18:
    print('Boa tarde!')
elif 18 <= horas < 24:
    print('Boa noite!')
else:
    print('Hora inválida!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Informe seu nome: ').strip().capitalize()
print(nome)

if len(nome) <= 4:
    print('Seu nome possui 4 letras ou menos.')
elif len(nome) <= 6:
    print('Seu nome possui de 5 a 6 letras. Nome comum.')
else:
    print('Seu nome é muito grande!')


# Calculdora operações básicas

# while True:
#     try:
#         print("""Menu de opções
#             1 - Adição [+]
#             2 - Subtração [-]
#             3 - Divisão [/]
#             4 - Multiplicação [*]
#             5 - Sair 
#             """)

#         op = float(input('Informe sua opção: '))

#         if op == 5:
#             print('Até a próxima!')
#             break

#         n1 = float(input('1° número: '))
#         n2 = float(input('2° número: '))

#         if op == 1:
#             resultado = n1 + n2
#             print(f'{n1} + {n2} = {resultado}')
#         elif op == 2:
#             resultado = n1 - n2   
#             print(f'{n1} - {n2} = {resultado}')
#         elif op == 3:
#             resultado = n1 / n2
#             print(f'{n1} / {n2} = {resultado}')
#         elif op == 4:
#             resultado = n1 * n2
#             print(f'{n1} * {n2} = {resultado}')
    
#     except ValueError:
#         print('Informe apenás números.')


# Analisando TEXTO

frase = 'isso é uma frase de texto e estamos estudando'

print(frase.count('é'))  # Contando quantas letras 'é' tem no texto

for palavra in frase:
    cont = palavra.count(all)

# # Exercicio

# nome = 'Rodrigo de Almeida Barros'
# altura = 1.82
# peso = 92
# imc = peso / (altura * altura)

# print(f'Nome: {nome}\nTem {altura} de altura\n{peso} de peso\n{imc:.2f} de índice de massa corporal.')

# """
# Interpolação de strings

# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCD01232223)

# """

# nome = 'rodrigo'
# preco = 100.9889889
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

usuario = str(input('Informe seu nome: '))
idade = int(input('Informe sua idade: '))

if usuario and idade:
    print(f'Seu nome é {usuario}')
    print(f'Seu nome invertido é {usuario[::-1]}')
    
    if ' ' in usuario:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {len(usuario.strip())} letras')
    print(f'A primeira letra do seu nome é {usuario[0]}')
    print(f'A ultima letra do seu nome é {usuario[-1]}')

else:
    print('Você não informou nada nos campos.')


        







            
