#é uma lista imutavel
#é um pouco mais rápida que a lista
nomes = "Carolina", "Eduardo", "Renato", "Eduardo"
nomes2 = ("Carolina", "Roberto", "Renato")

print(nomes)
#nomes[1] = "Renata" #não é permitido alterar os valores de uma tupla

print(nomes)
print()
print(nomes.count('Eduardo')) # diz quantas vezes o nome esta na tupla
print(nomes.index('Carolina'))# fala o indice onde esta o dado Carolina

#item é a variável que eu defini para receber cada um dos nomes isoladamente
for item in nomes:
    print(item)#a cada item do dicionário nomes ele joga o valor em item e printa na tela aqui

