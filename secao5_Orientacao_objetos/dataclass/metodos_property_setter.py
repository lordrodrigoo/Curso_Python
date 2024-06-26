from dataclasses import dataclass 

@dataclass
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30, 'Augusto')
    p2 = Pessoa('Luiz', 30, 'Augusto')
    print(p1 == p2)
    p1 = Pessoa('Rodrigo', 33, 'Almeida')
    p1.nome_completo = 'Rodrigo de Almeida'
    print(p1)
    print(p1.nome_completo)
    