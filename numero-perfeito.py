'''
Número perfeito: é um número onde a soma dos seus divisores positivos (exceto o próprio número) é igual a esse número
Exemplo: 6

6 = 1 + 2 + 3 = 6
'''

def numPerfeito(n):
	soma = 0
	for i in range(1, n):
		if n % i == 0:
			soma = soma + i

	if(soma == n):
		return 'Número perfeito'

	return 'Número imperfeito'

print(numPerfeito(496))