# PROJETO DE CRIAR UM GERENCIADOR DE SENHAS

import time

senhas = {}

while True:
    print("== GERENCIADOR DE SENHAS ==")
    time.sleep(1)
    print(" - MENU DE OPÇÕES -")
    time.sleep(1)
    print("1. Adicionar nova senha")
    print("2. Listar senhas")
    print("3. Buscar senha")
    print("4. Excluir senha")
    print("5. Sair")
    time.sleep(1)
    opcao = input("Escolha uma opção: ")
    if opcao == "1": # ADICIONAR NOVA SENHA
        nome = input("Digite o nome do serviço: ")
        senha = input("Digite a senha: ")
        senhas[nome] = senha
        print("Senha adicionada com sucesso!")
    elif opcao == "2": # LISTAR SENHAS
        print("== LISTA DE SENHAS ==")
        for nome, senha in senhas.items():
            print(f"Serviço: {nome} | Senha: {senha}")
    elif not senhas: # VERIFICA SE HÁ SENHAS CADASTRADAS
            print("Nenhuma senha cadastrada.")
            time.sleep(1)
            print("Reiniciando o gerenciador de senhas...")
            time.sleep(2)
    elif opcao == "3": # PROCURAR SENHAS
        nome = input("Digite o nome do serviço para buscar a senha: ")
        if nome in senhas:
            print(f"A senha para {nome} é: {senhas[nome]}")
        else:
            print("Serviço não encontrado.")
            time.sleep(1)
            print("Reiniciando o gerenciador de senhas...")
            time.sleep(2)
    elif opcao == "4": # EXCLUIR SENHA
        nome = input("Digite o nome do serviço para excluir a senha: ")
        if nome in senhas:
            del senhas[nome]
            print("Senha excluída com sucesso!")
        else:
            print("Serviço não encontrado.")
            time.sleep(1)
            print("Reiniciando o gerenciador de senhas...")
            time.sleep(2)
    elif opcao == "5": # SAIR
        print("Saindo do gerenciador de senhas...")
        time.sleep(2)
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(1)