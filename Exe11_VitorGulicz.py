#- Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
#Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
#O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
#No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
#Desenvolva um programa em Python que:
#1.	Solicite ao usuário o número de tarefas a serem inseridas.
#2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
#3.	Conte e exiba o número de tarefas concluídas e não concluídas.

numeroTarefas=int(input("Digite o numero de tarefas: "))
tarefaSim=0
tarefaNao=0

for i in range(numeroTarefas):
    op=str(input("A tarefa está completa?(sim ou s | não ou n)"))
    if "sim" in op.lower() or "s" in op.lower():
        tarefaSim+=1
    elif "não" in op.lower() or "s" in op.lower():
        tarefaNao+=1
    else:
        print("Opção invalida")
print("Tarefas concluidas:",tarefaSim,"\n Tarefas não concluidas:",tarefaNao,)
print("Vitor Gulicz")