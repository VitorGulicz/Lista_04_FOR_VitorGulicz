#Peça ao usuário para inserir o seu nome e um numero. Se o numero for menor que 10 exiba o nome dele esse numero de vezes caso contrario exiba a mensagem “numero muito alto”
# três vezes
nome=input("Insira seu nome: ")
numero=int(input("Digite um numero: "))
if numero<10:
    for i in range(numero):
        print(nome)
else:
    for i in range(3):
        print("Numero muito alto")