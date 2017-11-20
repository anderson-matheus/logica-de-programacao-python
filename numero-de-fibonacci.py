'''
Sequência de Fibonacci
1, 1, 2, 3, 5, 8...
'''

def fib(n):
	if n == 1 or n == 2:
		return 1

	lista = [1, 1]
	cont = 2
	while(cont <= n):
		lista.append(lista[cont-1] + lista[cont-2])
		cont += 1
	return lista[n]

termo = 7
print(fib(termo - 1))
