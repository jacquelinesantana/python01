print("ola mundo")
# comentário em linha
print("linha 2 de texto")
print("acentos de atenção")
"""   
multiplas linhas
no python - isso na verdade é um docString
útil para gerar documentação automática com ferramentas como o Sphinx
acessível via help() o interpletador do python
Documentação que precisa ser acessível em tempo de execução

Docstrings devem ser usadas para documentação formal 
que será útil para outros desenvolvedores que usarão seu código.
"""
# função print
print(1,2,"ola mundo","vamos ver aqui")
#1 2 são argumentos não nomeados
print(1,2,sep='¬')
# sep é um argumento nomeado ele tem um nome o sep é um argumento nomeado
print(1,2,3,end='**')
# end é um argumento nomeado, ele tem o nome end e altera o comportamento
#para o final da saída do print
print("próxima saída!")
print();
print(1,2,sep='_')

print('ola mundo \"denovo\" br')
print();

print(1,2,end="**")
print("novo texto")

print()
print("Jacqueline \"é deve Python\"")#o R no inicio permite ver os escapes do \ ""
print('Jacqueline "é deve Python", testando segundo scape de aspas')#o R no inicio permite ver os escapes do \ ""
print()
print("1" + "1")

print()
print(1.2)
print(1.5 * 2)
print(1+1)
print()

#ver tipo de dados
print( type(1.5) ) # classe type retorna o tipo de dado
print()
print(2)
print(2+3)
print()
print(2.8)
print(1.3+1.7)
print(0.5)
print()
print(True)
print(False)
print()
print(type('True'))
print(...)
print()
altura = 1.587894
saldo = 1587.6557841
print(f'{altura:.2f}')
print(f'{saldo:.2f}')

print()
nome = "João"
idade = 25
# Usando format()
texto = "Olá {}, você tem {} anos".format(nome, idade)
print(texto)
# Usando f-string (mais moderno)
texto = f"Olá {nome}, você tem {idade} anos"
print(texto)
# Precisão em números flutuantes
pi = "Pi: {:.5f}".format(3.14159265359)
# Resultado: "Pi: 3.14159"

# Truncamento de strings
texto = "{:.3}".format("Python")
# Resultado: "Pyt"
print(pi)
print(texto)
print()
nome = input("Qual o seu nome? ")
print("O usuário se chama:" + nome)

print()
lista = list();
print(lista)

print() 
lista2 = [];
lista3 = [1,True,"Rita de Cássia", 37, "desenvolvimento web"]
print(lista3)

print(type(lista3))