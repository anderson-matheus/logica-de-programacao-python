'''
Recursividade

Quando uma função chama a si própria
'''

def pot(base, exp):
	# caso base
	if exp == 0:
		return 1

	return base * pot(base, exp-1)

print(pot(2, 10))