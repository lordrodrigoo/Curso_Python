from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute()) 

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt' # Criando arquivo no local desejado.

caminho_arquivo.touch()
print(caminho_arquivo)

# arquivo.unlink()  # Apaga o arquivo

caminho_arquivo.write_text('qualquer coisa.\n')  # Escrevendo uma linha arquivo

# Escrevendo em varias linhas no arquivo 
with caminho_arquivo.open('a+', encoding='utf8') as file:
    file.write('Uma linha\n')
    file.write('mais linha\n')
    file.write('outra linha\n')

print(caminho_arquivo.read_text()) # lendo o arquivo

 # Criando uma pasta no local desejado.
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True) # Ignora se a pasta ja estiver criada
subpasta = caminho_pasta / 'subpasta' # criando subpasta
subpasta.mkdir(exist_ok=True)
 

