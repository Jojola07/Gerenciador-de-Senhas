# PROJETO DE CRIAR UM GERENCIADOR DE SENHAS

import time,json

senhas_file = "senhas.json"

# Carregar senhas do arquivo JSON, se existir
try:
    with open(senhas_file, "r") as f:
        senhas = json.load(f)
except FileNotFoundError:
    senhas = {}

def salvar_senhas():
    with open(senhas_file, "w") as f:
        json.dump(senhas, f, indent=4)   
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
        nome = input("Digite o nome do serviço: ").lower()
        if nome in senhas:
            substituir = input("Esse serviço já está no sistema, deseja substituir a senha? (s/n): ")
            if substituir.lower() != 's':
                print("Operação cancelada.")
                time.sleep(1)
                print("Voltando ao Menu...")
                time.sleep(2)
                continue
        senha = input("Digite a senha: ")
        senhas[nome] = senha
        salvar_senhas()
        print("Senha adicionada com sucesso!")
    elif opcao == "2":  # LISTAR SENHAS
        print("== LISTA DE SENHAS ==")
        if senhas:
            for nome, senha in senhas.items():

                print(f"Serviço: {nome.title()} | Senha: *******")
        else:
            print("Nenhuma senha cadastrada.")
            time.sleep(1)
            continue
    elif opcao == "3":  # PROCURAR SENHAS
        nome = input("Digite o nome do serviço para buscar a senha: ").lower()
        if nome in senhas:
            print(f"A senha para {nome.title()} é: {senhas[nome]}")
        else:
            print("Serviço não encontrado.")
            time.sleep(1)
            print("Voltando ao Menu...")
            time.sleep(2)
    elif opcao == "4": # EXCLUIR SENHA
        nome = input("Digite o nome do serviço para excluir a senha: ").lower()
        if nome in senhas:
            deletarConfirmacao = input(f"Tem certeza que deseja excluir a senha para {nome}? (s/n): ")
            if deletarConfirmacao.lower() != 's':
                print("Exclusão cancelada.")
                time.sleep(1)
                print("Voltando ao Menu...")
                time.sleep(2)
                continue
            else:
                del senhas[nome]
                salvar_senhas()
                print("Senha excluída com sucesso!")
        else:
            print("Serviço não encontrado.")
            time.sleep(1)
            print("Voltando ao Menu...")
            time.sleep(2)
    elif opcao == "5": # SAIR
        print("Saindo do gerenciador de senhas...")
        time.sleep(2)
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(1)
        print("Voltando ao Menu...")