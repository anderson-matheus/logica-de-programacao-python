#em dicionários a chave é única

d = {'marcos': 28, 'joao': 20, 'maria': 30}

print(d)
print(d['joao'])
print(d['maria'])

d['maria'] = 35
print(d['maria'])

if 'marcos' in d:
	print('Chave encontrada')
else:
	print('Chave não encontrada')