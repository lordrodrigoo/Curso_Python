# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args

# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import locale
import sys

print(sys.platform) # Win32

enconding = locale.getpreferredencoding() # Vendo qual a decodificação preferida do windows cp1252
# Más funciona legal no windows cp850

comando = ['ping', '127.0.0.1', '-c', '4']
enconding = 'utf_8'
sistema = sys.platform

if sistema == 'win32':
    comando = ['ping', '127.0.0.1']
    enconding = 'cp850'



processo = subprocess.run(comando, capture_output=True, text=True, encoding='cp850')
print(processo)
print()

# print(processo.args)
# print(processo.stderr)
print(processo.stdout)
# print(processo.returncode)
