def somarQuadrados(lista):
	soma = 0
	for num in lista:
		soma = soma + (num * num)
	return soma

lista = [1, 2, 3, 4]
result = somarQuadrados(lista)
print(result)