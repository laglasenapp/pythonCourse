nome = input('Informe o seu nome: ')
with open('exercicio3.txt', 'a') as arquivo:
    arquivo.write(f'{nome}\n')