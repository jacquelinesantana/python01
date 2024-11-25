lista = list()
print(lista)

lista_a = [10, 20, 30, 40]
lista_b = [45,55,65,75]

lista = lista_a + lista_b
print(lista)

lista_a.extend(lista_b)


print(lista_a)
lista_b.insert(10, 85)
print()
print(lista_a)
print(lista_b)