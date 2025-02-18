#Defina uma variável chamada total como 0. peça ao usuário para inserir 5 números e após cada entrada e pergunte se ele deseja deva ser incluído (S ou s, N ou n). Se ele desejar 
# adicione o numero ao total. Se ele não quiser não adicione ao total. Depois de inserir o numero 5 vezes exiba o total.
total=0
for i in range(5):
    numero=float(input("Digite um numero: "))
    op=(input("Deseja adicionar um numero ao total?(s ou n): "))
    if "s" in op.lower():
        total=total+numero
    else:
        print("Numero não adicionado")
print("Numero total: ",total)