'''
Exemplos de números primos?

7, 11, 13, ...
'''

def primo(n):
	contDiv = 0
	for i in range(1, n+1):
		if n % i == 0:
			contDiv += 1

	if contDiv <= 2:
		return True
	
	return False

print(primo(11))
