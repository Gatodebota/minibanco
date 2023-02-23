menu = """

[s] Sacar
[d] Depositar
[e] Extrato
[q] sair
    
"""

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)


    if opcao == "d":
        valor = float(input("valor do deposito"))
        if valor>0:
            saldo+=valor
            extrato+=f"Deposito:R$ {valor:.2f}\n"
        else:
            print("valor incorreto")

    elif opcao =="s":
        valor = float(input("informe o valor do saque"))

        execeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques == LIMITE_SAQUES

        if execeu_saldo:
            print("voce nao tem saudo suficente")
        elif excedeu_limite:
            print("excedeu limite")
        elif execeu_saldo:
            print("excedeu saques")

        elif valor>0:
            saldo -= valor
            extrato += f"saque : R$ {valor:.2f}\n"
            numero_saques +=1

        else:
            print("numero invalido")

    elif opcao =="e":
        print("\n========================= EXTRATO =====================")
        print("nao foram realizadas movimentacoes" if not extrato else extrato)
        print(f"\n saldo: Rs {saldo:.2f}")

    elif opcao =="q":
        break

    else:
        print("operacao invalida")
