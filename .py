contatos = []

def exibir_menu():
    print("\n" + "="*40)
    print("📞  GERENCIADOR DE CONTATOS")
    print("="*40)
    print("1 - Adicionar Contato")
    print("2 - Listar Contatos")
    print("3 - Buscar Contato")
    print("4 - Remover Contato")
    print("5 - Sair")

def adicionar_contato():
    print("\n🔹 ADICIONAR CONTATO")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    if nome == "" or telefone == "" or email == "":
        print("⚠️ Todos os campos devem ser preenchidos.")
        return

    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print("✅ Contato adicionado com sucesso!")

def listar_contatos():
    print("\n📋 LISTA DE CONTATOS")
    if not contatos:
        print("⚠️ Nenhum contato para exibir.")
        return

    print("-"*60)
    print("{:<20} {:<15} {:<25}".format("NOME", "TELEFONE", "E-MAIL"))
    print("-"*60)
    for c in contatos:
        print("{:<20} {:<15} {:<25}".format(c["nome"], c["telefone"], c["email"]))
    print("-"*60)

def buscar_contato():
    nome_busca = input("\n🔍 Digite o nome para buscar: ").strip().lower()
    encontrados = [c for c in contatos if nome_busca in c["nome"].lower()]

    if encontrados:
        print("\n✅ CONTATOS ENCONTRADOS:")
        print("-"*60)
        print("{:<20} {:<15} {:<25}".format("NOME", "TELEFONE", "E-MAIL"))
        print("-"*60)
        for c in encontrados:
            print("{:<20} {:<15} {:<25}".format(c["nome"], c["telefone"], c["email"]))
        print("-"*60)
    else:
        print("❌ Nenhum contato encontrado com esse nome.")

def remover_contato():
    nome_remover = input("\n🗑️ Digite o nome do contato a remover: ").strip().lower()
    for i, c in enumerate(contatos):
        if nome_remover == c["nome"].lower():
            del contatos[i]
            print("✅ Contato removido com sucesso!")
            return
    print("❌ Contato não encontrado.")


while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("👋 Saindo do programa... Até logo!")
        break
    else:
        print("⚠️ Opção inválida! Tente novamente.")
