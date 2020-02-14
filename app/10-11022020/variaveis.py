
#str para String
nome = 'Luiz'

# inteiros
idade = 10

# float
try:
    salario = float(input('Digite seu salário: '))
    print(f'O salário informado foi {salario}')
except ValueError:
    print('Não foi informado um valor inválido!')

# Função bool
verdadeiro = True
falso = False
 
obj = None
print(type(obj))
