import datetime

produtos = {}
funcionarios = {}
estoque = {}
vendas = []

# Menu
def exibir_menu():
    print("========== MENU CAFETERIA ==========")
    print("1. Realizar Venda")
    print("2. Gerenciar Estoque")
    print("3. Gerenciar Funcionários")
    print("4. Comunicação Terceirizada")
    print("5. Exibir Relatórios")
    print("0. Sair")
    print("====================================")

# realizar uma venda
def realizar_venda():
    produto = input("Informe o produto vendido: ")
    quantidade = int(input("Informe a quantidade vendida: "))
    funcionario = input("Informe o nome do funcionário responsável: ")

    if produto in estoque and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        vendas.append({"produto": produto, "quantidade": quantidade, "funcionario": funcionario})
        print("Venda realizada com sucesso!")
    else:
        print("Produto não disponível em estoque ou quantidade insuficiente.")

# adicionar um novo produto no estoque
def adicionar_produto():
    produto = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade inicial: "))

    produtos[produto] = quantidade
    estoque[produto] = quantidade
    print("Produto adicionado ao estoque.")

# remover um produto do estoque
def remover_produto():
    produto = input("Informe o nome do produto a ser removido: ")

    if produto in produtos:
        del produtos[produto]
        del estoque[produto]
        print("Produto removido do estoque.")
    else:
        print("Produto não encontrado.")

# mudar a quantidade de um produto no estoque
def atualizar_estoque():
    produto = input("Informe o nome do produto a ser atualizado: ")

    if produto in estoque:
        quantidade = int(input("Informe a nova quantidade: "))
        estoque[produto] = quantidade
        print("Estoque atualizado.")
    else:
        print("Produto não encontrado.")

# adicionar um novo funcionário
def adicionar_funcionario():
    nome = input("Informe o nome do funcionário: ")
    funcionarios[nome] = {"pontos": 0, "frequencia": 0}
    print("Funcionário adicionado.")

# remover um funcionário
def remover_funcionario():
    nome = input("Informe o nome do funcionário a ser removido: ")

    if nome in funcionarios:
        del funcionarios[nome]
        print("Funcionário removido.")
    else:
        print("Funcionário não encontrado.")

# horário de entrada e saída e bater ponto
def bater_ponto():
    funcionario = input("Informe o nome do funcionário: ")

# horário de entrada
    while True:
        horario_entrada = input("Informe o horário de entrada (HH:MM): ")
        try:
            hora, minutos = map(int, horario_entrada.split(":"))
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                break
            else:
                print("Horário inválido. Insira um valor no formato HH:MM e dentro do intervalo 00:00 a 23:59.")
        except ValueError:
            print("Formato inválido. Insira o horário no formato HH:MM.")

    # horário de saída
    while True:
        horario_saida = input("Informe o horário de saída (HH:MM): ")
        try:
            hora, minutos = map(int, horario_saida.split(":"))
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                break
            else:
                print("Horário inválido. Insira um valor no formato HH:MM e dentro do intervalo 00:00 a 23:59.")
        except ValueError:
            print("Formato inválido. Insira o horário no formato HH:MM.")

    # Registrar ponto
    pontos_funcionario = funcionarios.get(funcionario, {}).get("pontos", [])
    pontos_funcionario.append({"entrada": horario_entrada, "saida": horario_saida})
    funcionarios[funcionario] = {
        "pontos": pontos_funcionario,
        "frequencia": len(pontos_funcionario)
    }

    print("Ponto registrado com sucesso.")

# frequência diária dos funcionários
def frequencia_diaria():
    data_atual = datetime.date.today()

    for funcionario in funcionarios:
        pontos_funcionario = funcionarios[funcionario].get("pontos", [])

        if any("data" in ponto and ponto["data"] == data_atual for ponto in pontos_funcionario):
            print(f"Frequência já registrada para o funcionário {funcionario} na data de hoje.")
        else:
            pontos_funcionario.append({"data": data_atual, "frequencia": 1})
            funcionarios[funcionario]["pontos"] = pontos_funcionario
            print(f"Frequência registrada para o funcionário {funcionario} na data de hoje.")

# comunicar com as empresas terceirizadas
def comunicar_empresa_terceirizada():
    empresa = input("Informe o nome da empresa terceirizada: ")
    produto = input("Informe o produto a ser reposto: ")
    quantidade = int(input("Informe a quantidade a ser reposta: "))

    # -> Codigo ou forma de comunicação com a empresa terceirizada (depende da empresa que for, e do contrato que tiverem) <-

    print(f"Reposição de estoque solicitada para a empresa {empresa}. Para o produto: {produto}, Quantidade: {quantidade}.")

# exibir os relatórios
def exibir_relatorios():
    print("========== RELATÓRIOS ==========")
    print("Relatório de Vendas:")
    for venda in vendas:
        print(f"Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Funcionário: {venda['funcionario']}")
    print("Relatório de Estoque:")
    for produto, quantidade in estoque.items():
        print(f"Produto: {produto}, Quantidade: {quantidade}")
    print("Relatório de Funcionários:")
    for nome, dados in funcionarios.items():
        print(f"Funcionário: {nome}, Pontos: {dados['pontos']}, Frequência: {dados['frequencia']}")
    print("================================")

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Informe a opção desejada: ")

    if opcao == "1":
        realizar_venda()
    elif opcao == "2":
        print("========== GERENCIAR ESTOQUE ==========")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Atualizar Estoque")
        print("0. Voltar")
        print("=======================================")
        opcao = input("Informe a opção desejada: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "0":
            continue
        else:
            print("Opção inválida.")
    elif opcao == "3":
        print("========== GERENCIAR FUNCIONÁRIOS ==========")
        print("1. Adicionar Funcionário")
        print("2. Bater Ponto")
        print("3. Registro de Frequência Diária")
        print("4. Remover Funcionário")
        print("0. Voltar")
        print("============================================")
        
        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            bater_ponto()
        elif opcao == "3":
            frequencia_diaria()
        elif opcao == "4":
            remover_funcionario()
        elif opcao == "0":
            continue
        else:
            print("Opção inválida.")
    elif opcao == "4":
        comunicar_empresa_terceirizada()
    elif opcao == "5":
        exibir_relatorios()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")

# FIM
