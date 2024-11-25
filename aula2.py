lista = [1, True, "Rodrigo", "Analista de Redes"]
print(lista[2])

lista[0] = 15

print(lista)

del lista[1] 
#evitar usar o del porque ele precisa mover todos os itens restantes 
#após o indice removido e isso dependendo da quantidade total de itens
#pode requerer muito processamento 
#indicado para remover itens no final da lista
print(lista)
print(lista[1])

lista.append("novodado")
#adicionar itens ao final da lista

print(lista)
item_removido = lista.pop() #joga o valor removido e remove
lista.pop()
#remove o ultimo item da lista
print(lista)
lista.clear()
print(lista)
lista.append(10)
lista.append("Marcia")
print(lista)
lista.insert(2, 'Desenvolvedora Front end')
print(lista)
lista.insert(4,5800.57)
print(lista)
print(lista[2])
lista.insert(0, 2)
#ao realizar o insert para um indice muito alto, maior que o que tem na lista
#ele insere no final da lista
print(lista)
print()
