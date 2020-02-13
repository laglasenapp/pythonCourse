with open('exercicio3.txt','r') as arquivo:
    for l in arquivo:
        print(f'Nome: {l.strip()}')