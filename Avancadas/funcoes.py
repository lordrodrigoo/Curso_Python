"""
HIgher Order Functions
Funções de primeira classe

"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Rodrigo')
print(v)

"""
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados
 diferentes.
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns
 (strings, inteiros, etc...)
Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.
Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""
####################################################################################################

"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))