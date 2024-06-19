from ex_classes import CAMINHO, Pessoa
import json

with open(CAMINHO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])    
    p2 = Pessoa(**pessoas[1])    
    p3 = Pessoa(**pessoas[2])    
    p4 = Pessoa(**pessoas[3])    

    print(p1.nome, p1.sobrenome, p1.idade)
    print(p2.nome, p2.sobrenome, p2.idade)
    print(p3.nome, p3.sobrenome, p3.idade)
    print(p4.nome, p4.sobrenome, p4.idade)



