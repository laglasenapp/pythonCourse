#Impressao
#Documentar as linhas Ctrl + k + c
#Documentar as linhas Ctrl + k + u
# print('Java is easier than Python!')
# print('Java ist einfacher als Python! Scheisse!')
# print('Luiz'[0:3:2])
# print('Luiz ' * 10)
# print('Luiz ' + 'Glasenapp')
# print('\n')

#Pegar as informações do usuário
nome = input('Informe seu nome: ')
print(type(nome))
nome = 1234
print(type(nome))
sobrenome = input('Informe seu sobrenome: ')

#Usando a função format para concatenação de String
print('Olá {}'.format(nome))
print('Olá {} {}'.format(nome, sobrenome))

#Interpolação de String
print(f'Olá {nome} {sobrenome}')

try:
    idade = int(input('Idade: '))
    print(idade)
except ValueError:
    print('Animal!!!! Você não informou uma letra!!!')