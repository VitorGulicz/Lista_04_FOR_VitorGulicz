#Peça um numero abaixo de 50 e em seguida faça uma contagem regressiva de 50 até esse numero, certificando-se de mostrar o numero que eles inseriram na saída
numero=int(input("Digite um numero abaixo de 50: "))
if numero<=50:
    for i in range(50 ,numero -1,-1):
            print(i)
    print("Vitor Gulicz")
else:
    print("Numero invalido -Vitor Gulicz")