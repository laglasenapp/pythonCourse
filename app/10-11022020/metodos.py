
def cadastro():
    nome = input('nome: ')
    sobrenome = input('sobrenome: ')
    telefone = input('telefone: ')
    cliente = {'nome':nome, 'sobrenome':sobrenome, 'telefone':telefone}
    return cliente

def imprimir(cliente):
    nome = cliente['nome']
    sobrenome = cliente['sobrenome']
    telefone = cliente['telefone']
    print(f'{nome} {sobrenome} {telefone}')
    print(f"{cliente['nome']};{cliente['sobrenome']};{cliente['telefone']}")

c = cadastro()
imprimir(c)

