#listas com dados mutaveis
lista_a = ["joão", "maria"]
lista_b = lista_a
#lista_b esta apontando para o mesmo dados que a lista_a não estou copiando a lista_a
print(lista_b)
#copiar a lista e deixar independentes
lista_c = lista_a.copy()
lista_a[1] = "Rosa"
print(lista_b)
print(lista_c)

