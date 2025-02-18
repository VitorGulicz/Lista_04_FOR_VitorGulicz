#Faça um programa um programa que solicite ao usuário para digitar o seu nome e um numero qualquer e em seguida exiba seu nome varias vezes de acordo com o número inserido
nome=input("Insira seu nome: ")
numero=int(input("Digite um numero: "))
for i in range(numero):
    print(nome)