from funcionario import Funcionario
dic = {}
def cadastrarFuncionario():
    nome = input('Informe o nome: ')
    rg = input('Informe o RG: ')
    funcionario = Funcionario(nome, rg)
    dic.update({'funcionario':funcionario})

def imprimir():
    valor = dic['funcionario']
    print(valor)

cadastrarFuncionario()
imprimir()