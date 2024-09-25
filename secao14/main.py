from calculadora import soma

# https://docs.python.org/pt-br/3/library/doctest.html
# https://docs.python.org/pt-br/3/library/unittest.html

# print(soma(10, 20))
# print(soma(1.5, 2.5))
# print(soma(-10, 20))
print(soma('15', 15))


try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')