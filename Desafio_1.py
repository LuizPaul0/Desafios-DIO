
menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
    
    => """

saldo = 0
limite =500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("VALOR INVALIDO!")
            
    

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo_inferior = valor > saldo

        limite_excedido = valor > limite

        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_inferior:
            print("Saldo insuficiente!")

        elif limite_excedido:
            print("Limite para saque exedido!")

        elif saque_excedido:
            print("O numero de saques diarios foi exedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação realizada com sucesso!")

        else:
            print("Erro na operação! Valor inválido")


    elif opcao == "e":
        print("\n_____________________EXTRATO__________________")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("______________________________________________")
        

    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")