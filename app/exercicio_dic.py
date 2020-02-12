#cervejas = {'marca':'skol','tipo':'pilsen'}

#cervas = {}

#marca = input('Digite a marca da cerveja: ')
#tipo = input('Digite o tipo da cerveja: ')

#cervas['marca'] = marca
#cervas['tipo'] = tipo

#print(cervas)

pessoas = {}

for x in range(0, 2):
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    cpf = input('Informe o cpf: ')
    pessoas.update({f'nome{x}' : nome, f'sobrenome{x}' : sobrenome, f'cpf{x}' : cpf})    

print(pessoas)

id = None
try:
    id = input('Informe um id para ser removido do mapa: ')
    del pessoas[f'nome{id}']
    del pessoas[f'sobrenome{id}']
    del pessoas[f'cpf{id}']
except KeyError:
    print(f'Id informado não existe! Id: {id}')
print(pessoas)


