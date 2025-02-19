#- Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
pessoasFesta=int(input("Digite o numero de pessoas que deseja convidar para a festa: "))
if pessoasFesta<10:
    
    for i in range(pessoasFesta):
        nome=input("Digite o nome da pessoa: ")
        print(nome,"está convidado para a festa")
    print("Vitor Gulicz")
else:
    print("Muitas pessoas! - Vitor Gulicz")