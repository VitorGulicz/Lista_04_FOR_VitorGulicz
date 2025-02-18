#Escreva um programa para pedir um numero e em seguida o nome. Exiba o nome(Uma letra de cada vez em cada linha) e repita isso para o numero de vezes que ele digitou
nome=input("Insira seu nome: ")
numero=int(input("Digite um numero: "))
for a in range(numero):
    for i in nome:
        print(i)