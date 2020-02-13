class Bebida:

    nome : None
    teor: None

    def __init__(self, nome, teor):
        self.nome = nome
        self.teor = teor
    
    def __str__(self):
        return f'Nome: {self.nome} Teor alcoólico:{self.teor}'
