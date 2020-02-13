class Funcionario:

    nome : None
    rg: None

    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg
    
    def __str__(self):
        return f'Nome: {self.nome} RG:{self.rg}'
