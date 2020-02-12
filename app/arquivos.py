dic = {}

def cadastrar_cerveja():
    dic['nome'] = input('Informe o nome da cerveja: ')
    dic['tipo'] = input('Informe o tipo da cerveja: ')

def gravar_arquivo():
    #arquivo = open('cerveja','a')
    #arquivo.write(dic['nome'] + ';' + dic['tipo'] )
    #arquivo.close()
    with open('cerveja','a') as arquivo:
        arquivo.write(dic['nome'] + ';' + dic['tipo'] + '\n')

def ler_arquivo():
    #arquivo = open('cerveja','r')
    #for c in arquivo:
    #    print(c.strip())
    #arquivo.close()
    with open('cerveja','r') as arquivo:
        for c in arquivo:
            print(c.strip())

cadastrar_cerveja()
gravar_arquivo()
ler_arquivo()

