from Pessoa import Pessoa as pe

p = pe('Luiz','Glasenapp',25,'M')

print(p)

print(p.get_nome())

p.set_nome('Rebeca')

print(p.get_nome())