# lista []
# tupla
dicionario = {'Rebeca':'23','Luiz':'25'}
#print(dicionario['Rebeca'])

for x in dicionario:
    print(x)

pessoa1 = {'nome':'Luiz','sobrenome':'Glasenapp', 'idade': 25}
pessoa2 = {'nome':'Luiz1','sobrenome1':'Glasenapp1', 'idade': 26}
pessoa3 = {'nome':'Luiz2','sobrenome2':'Glasenapp2', 'idade': 27}
lista = []
lista.append(pessoa1)
lista.append(pessoa2)
lista.append(pessoa3)

for p in lista:
    print(p['nome'])