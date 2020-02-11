lista = []
lista = ['Luiz','Alfonso','Glasenapp']
print(lista)
print(lista[3:2:-1])
print(len(lista))

#for x in lista:
#    print(x[1:3])
print('---------')
lista.sort()
print('---------')

#foreach
for x in range(0, len(lista)):
    print(lista[x])

#reverso
for x in reversed(range(0, len(lista))):
    print(lista[x])

lista2 = [x if 'u' in x.lower() else None for x in lista]
#print(lista2)