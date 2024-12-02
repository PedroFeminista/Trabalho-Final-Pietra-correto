tabela_fipe = {
    #BMW
    'BMW M2 Competition': 389000,
    'BMW M5 Competition': 777000,
    'BMW M4 Competition': 830000,
    #Audi
    'Audi R8': 1902000,
    'Audi RS6 Avant': 1141000,
    'Audi TT': 297000,
    #Mercedes
    'Mercedes CLA 180': 129000,
    'Mercedes AMG-GT': 2000000,
    'Mercedes G63': 1860000,
    #Porsche
    'Porsche 911 Carrera': 1000000,
    'Porsche 911 GT3 RS': 2227000,
    'Porsche Cayenne': 990000,
    #Lamborghini
    'Lamborghini Urus': 3754000,
    'Lamborghini Aventador': 9043000,
    'Lamborghini Revuelto': 8090000
}

#veículos disponíveis na concessionária
veiculos_disponiveis = ['BMW M2 Competition', 'BMW M4 Competition', 'BMW M5 Competition', 'Audi R8', 'Audi RS6 Avant', 'Audi TT', 'Mercedes CLA 180', 'Mercedes AMG-GT', 'Mercedes G63', 'Porsche 911 Carrera', 'Porsche 911 GT3 RS', 'Porsche Cayenne', 'Lamborghini Urus', 'Lamborghini Aventador', 'Lamborghini Revuelto']

# Funções do sistema
def exibir_menu():
    print("\n--- Menu ---")
    print("1. Vender veículo")
    print("2. Alugar veículo")
    print("3. Comprar veículo")
    print("4. Sair")
    return input("Escolha uma opção: ")

def vender_veiculo(cliente):    
    marca_modelo = input("Informe a marca e modelo do veículo: ")
    if marca_modelo in tabela_fipe:
        valor_fipe = tabela_fipe[marca_modelo]
        proposta = valor_fipe * 0.88  # 12% de desconto
        aceitar = input(f"Proposta de venda: R${proposta:.2f}. Aceitar? (s/n): ")
        if aceitar.lower() == 's':
            cliente['saldo'] += proposta
            veiculos_disponiveis.append(marca_modelo)
            print(f"Veículo vendido! Seu novo saldo é R${cliente['saldo']:.2f}.") #da a mensagem de venda concluida e fala o novo saldo do cliente (o restante do dinheiro em conta)
        else:
            print("Venda cancelada.")
    else:
        print("Veículo não encontrado na tabela FIPE.")

def alugar_veiculo(cliente):
    print("Veículos disponíveis para aluguel:")
    for veiculo in veiculos_disponiveis:
        print(veiculo)

    escolha = input("Escolha um veículo para alugar: ") #Aqui é onde a pessoa vai escolher o veículo que quer.
    if escolha in veiculos_disponiveis:
        dias = int(input("Informe o número de dias desejados: "))
        custo_total = dias * 77
        if cliente['saldo'] >= custo_total: #Confer se o saldo do cliente é compatível com a ação
            cliente['saldo'] -= custo_total
            veiculos_disponiveis.remove(escolha)
            print(f"Veículo alugado por {dias} dias. Seu novo saldo é R${cliente['saldo']:.2f}.")
        else:
            print("Saldo insuficiente para o aluguel.")
    else:
        print("Veículo não disponível para aluguel.")

def comprar_veiculo(cliente):
    print("Veículos disponíveis para compra:") #mostra os veículos que estão disponiveis para comprar
    for veiculo in veiculos_disponiveis:
        print(veiculo)

    escolha = input("Escolha um veículo para comprar: ")
    if escolha in veiculos_disponiveis:
        valor_fipe = tabela_fipe[escolha]
        valor_compra = valor_fipe * 1.25  # 25% de acréscimo
        if cliente['saldo'] >= valor_compra: #if também para conferir o saldo
            cliente['saldo'] -= valor_compra
            veiculos_disponiveis.remove(escolha)
            print(f"Veículo comprado! Seu novo saldo é R${cliente['saldo']:.2f}.")
        else:
            print("Saldo insuficiente para a compra.") #se não tiver saldo suficiente
    else:
        print("Veículo não disponível para compra.") #Se escolher um veículo que não está na concessionária.

def main():
    # Aqui é onde entram as informações do cliente
    cliente = {}
    cliente['nome'] = input("Informe seu nome: ")
    cliente['telefone'] = input("Informe seu telefone: ")
    cliente['saldo'] = float(input("Informe seu saldo disponível: R$"))

    while True:
        opcao = exibir_menu()
        if opcao == '1':
            vender_veiculo(cliente)
        elif opcao == '2':
            alugar_veiculo(cliente)
        elif opcao == '3':
            comprar_veiculo(cliente)
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")  
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()