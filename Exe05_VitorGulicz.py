#Peça ao usuário para inserir um numero que deseja a tabuada e em seguida exibir a tabuada desse numero digitado
numero=int(input("Digite um numero para ser feiro a tabuada: "))
for i in range(10):
    print(numero,"X",i,"=",numero*i)