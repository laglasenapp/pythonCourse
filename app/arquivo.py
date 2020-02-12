nome = 'Luiz'
sobrenome = 'Glasenapp'

arquivo = open('pessoa.txt', 'a')
arquivo.write(f'{nome};{sobrenome}\n')
arquivo.close()
print(arquivo.closed)


arquivoL = open('pessoa.txt', 'r')
for l in arquivoL:
    #remover quebra de linha
    print(l.strip())

