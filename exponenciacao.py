'''
base e expoente

Exemplo:
base = 2
expoente: 3

2^3 = 2 * 2 * 2 = 8
'''


def potencia(base, expoente):
	resultado = 0

	if(expoente == 0):
		return 1

	resultado = base
	while(expoente > 1):
		resultado *= base
		expoente -= 1
	return resultado

print(potencia(3, 3))