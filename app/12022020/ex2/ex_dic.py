from bebida import Bebida

dic = {}
def cadastrarFuncionario():
    nome = input('Informe o nome da cerveja: ')
    teor = int(input('Informe o teor alcoólico: '))
    bebida = Bebida(nome, teor)
    dic.update({'bebida':bebida})

def imprimir():
    valor = dic['bebida']
    print(valor)

cadastrarFuncionario()
imprimir()