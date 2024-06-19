"""
Faça uma lista de comprar com listas. O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os
from colorama import Fore as cor
from time import sleep
import re
def linha():
    print(cor.CYAN+'=' * 50)

lista = []
while True:
    
    print(cor.CYAN +"""Menu de opções
======== lista ========
1 - Adicionar Produto
2 - Listagem completa
3 - Apagar produto
4 - Sair""")
            

    op = int(input('Informe a opção: '))
    if op == 4:
        print(cor.LIGHTYELLOW_EX+'Saindo do programa...Até a próxima.')
        break
        

    elif op == 1:
        produto = str(input('adicionar produto: ')).title()
        if re.match(r"^[A-Za-z\s]+$", produto):  # Regex tratando input pra saber se TODOS são letras.
            lista.append(produto)
            print(cor.GREEN+f'{produto} foi adicionado com sucesso!')
            linha()
            sleep(1.6)
        else:
            print('Por favor, informe apenás letras sem acentos.')
    elif op == 2:
        if len(lista) == 0:
            print('A lista no momento está vazia.')
        linha()    
        print(cor.GREEN + '=== Lista de produtos ===')
        for i, produto in enumerate(lista):
            print(cor.GREEN+f'{i + 1}° - {produto}' )    
        linha()
    elif op == 3:
        if len(lista) == 0:
            print(cor.GREEN+'A lista no momento está vazia.')
        else:
            try:
                linha()
                print(cor.GREEN + '=== Lista de produtos ===')
                for i, produto in enumerate(lista):
                    print(cor.GREEN+f'{i + 1}° - {produto}' )
                indice = int(input(cor.CYAN+'Informe o índice da pessoa que deseja remover da lista: ')) -1
                remove = lista.pop(indice)
                linha
                print(f'{cor.GREEN+remove} foi removido da lista.')
            except ValueError:
                print(cor.RED+'Informe apénas números inteiro.')
            except IndexError:
                print(cor.RED+'Índice não encontrado...')

             




