#Faça um programa que pergunte em qual direção o usuário deseja contar (C ou c “Cima”, B ou b “Baixo”) Se ele selecionar para cima peça um numero superior e conte de 1 até 
# esse numero. Se ele selecionar baixo peça para inserir um numero abaixo de 20 e em seguida faça a contagem de 20 até esse numero. Se ele inserir opção diferente exiba a 
# mensagem direção invalida.
op=input("Digite qual direção deseja contar (c para cima | b para baixo): ")
#Direção Cima
if "c" in op.lower():
    numero=int(input("Digite um numero superior a 1: "))
    if numero>1:
        for i in range(numero):
            i=i+1
            print(i)
        print("Vitor Gulicz")
        #Direção Baixa
if "b" in op.lower():
    numero=int(input("Digite um numero inferior a 20: "))
    if numero<20:
        for i in range(20, numero-1, -1):
                print(i)
        print("Vitor Gulicz")
        #Caso opçao ivalida
    else:
        print("Numero invalido -Vitor Gulicz")
else:
    print("Direção invalida -Vitor Gulicz")
