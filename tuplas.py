#tupla não pode ser modificada, para se modificar deve se usar uma lista

tupla = (10, 5, 20)
lista = list(tupla)
lista[1] = 200;

tupla = tuple(lista)
print(tupla)