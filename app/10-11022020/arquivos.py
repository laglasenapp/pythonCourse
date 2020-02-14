dic = {}

def cadastrar_cerveja():
    nome = input('Informe o nome da cerveja: ')
    tipo = input('Informe o tipo da cerveja: ')
    dic.update({'nome':nome, 'tipo':tipo})

def gravar_arquivo():
    with open('cerveja','a') as arquivo:
        arquivo.write(dic['nome'] + ';' + dic['tipo'] + '\n')

def ler_arquivo():
    with open('cerveja','r') as arquivo:
        for c in arquivo:
            vetor = c.strip().split(';')
            print(vetor[0] + ' ' + vetor[1])

cadastrar_cerveja()
gravar_arquivo()
ler_arquivo()

