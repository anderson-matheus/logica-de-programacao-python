lista = [1, 2, 3, 4, 5]

print(lista)
print(len(lista))

for i in range(len(lista)):
	print(lista[i])

soma = 0

for e in lista:
	soma = soma + e

print(soma)