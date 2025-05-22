tarefas = []

def exibir_menu():
    print("\n MENU - LISTA DE TAREFAS")
    print("=" * 30)
    print("1 - Adicionar nova tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print(" Tarefa adicionada com sucesso!")
    else:
        print(" A tarefa não pode estar vazia.")

def visualizar_tarefas():
    print("\n TAREFAS ATUAIS:")
    if not tarefas:
        print(" Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")

def remover_tarefa():
    if not tarefas:
        print(" A lista de tarefas está vazia.")
        return

    print("\n REMOVER TAREFA")
    visualizar_tarefas()
    opcao = input("Digite o número ou nome da tarefa que deseja remover: ").strip()

    if opcao.isdigit():
        indice = int(opcao) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f" Tarefa '{removida}' removida com sucesso!")
        else:
            print(" Número inválido.")
    else:
        if opcao in tarefas:
            tarefas.remove(opcao)
            print(f" Tarefa '{opcao}' removida com sucesso!")
        else:
            print(" Tarefa não encontrada.")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        visualizar_tarefas()
    elif escolha == "3":
        remover_tarefa()
    elif escolha == "4":
        print(" Saindo da lista de tarefas... Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.")