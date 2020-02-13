# Criar um método que recebe dos numeros inteiros
# Metodos calcula a soma dos dois números e armazena em uma variável
# Metodo retorna a variavel com o resultado
# Imprimir o retorno do método

def receber_numeros():
    num = []
    for i in range(0,2):
        num.append(int(input('Informe um número inteiro: ')))
    return num    

def somar(numeros):
    return numeros[0] + numeros[1]

numeros = receber_numeros()
soma = somar(numeros)
print(f'A soma dos métodos é : {soma}')
