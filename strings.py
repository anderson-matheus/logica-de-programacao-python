#String não permite atribuições, ela é imutável
nome = 'Anderson'
lista = list(nome)
print(lista)

lista[0] = 'E'
nome = ''.join(lista)
print(nome)

s1 = 'Anderson'
s2 = ' Matheus'
s3 = s1 + s2
print(s3)
