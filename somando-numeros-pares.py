def somarPares(lista):
	soma = 0
	for num in lista:
		if(num % 2 == 0):
			soma += num
	return soma

lista = [10, 5, 7, 9, 20, 2]
result = somarPares(lista)
print(result)