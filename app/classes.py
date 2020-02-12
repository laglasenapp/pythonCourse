class Pessoa:

    nome = ''
    sobrenome = ''
    idade=0

    def incrementar(self, idade):
        idade = idade + 1
        print(idade)

    def imprimir(self):
        print(f'{self.nome};{self.sobrenome}')

    def __str__(self):
        return f'{self.nome};{self.sobrenome}'

    

p1 = Pessoa() 
p1.nome = 'Luiz'
p1.sobrenome = 'Glasenapp'
p1.imprimir()

p2 = p1
p2.incrementar(10)
p2.nome = 'Rebeca'
print(p1)
