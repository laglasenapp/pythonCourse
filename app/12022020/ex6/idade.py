# Criar um método para ler a idade de uma pessoa, converter para inteiro
# armazenar o dado em uma variável
# retornar o dado lido
# imprimir o retorno do método

def ler_idade():
    return int(input('Informe a idade: '))


idade = ler_idade()
print(f'Idade: {idade}')