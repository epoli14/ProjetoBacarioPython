menu = f"""

    #### BEM VINDO AO SISTEMA DO BANCO ###
    
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

"""

saldo, limite, saque_dia = 0.0, 500.0, 0
LIMITES_SAQUE_DIARIO = 3
depositos_dia = []
saques_dia = []

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar:\n"))
        depositos_dia.append(valor_deposito)
        saldo += valor_deposito

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar:\n"))

        if (saque_dia < LIMITES_SAQUE_DIARIO):

            if (valor_saque <= 500):
                saque_dia+= 1
                saques_dia.append(valor_saque)
                saldo-= valor_saque
                print(f"""Saque realizado com sucesso, saldo atualizado.
saldo: {saldo}""")
            else:
                print(f"""Valor indisponível.
saldo: {saldo}""")

        else:
            print("Seu limite de saques já foi atingido por hoje.")

    elif opcao == "e":
        if len(depositos_dia) > 0:
            print(f"Depositos do dia")
            for depositos in depositos_dia:
                print(f"R$ {depositos}")

        if len(saques_dia) > 0:
            print(f"Saques do dia")
            for saque in saques_dia:
                print(f"R$ {saque}")

        print(f"Saldo: {saldo}")
        break

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
