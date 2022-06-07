def calculadoraGorjeta():
    while True:
        conta = float(input("\nInforme o valor total do consumo: R$ "))
        pessoas = int(input("Informe o total de pessoas: "))
        if pessoas < 1:
            print("Valor invalido")
            break
        percentualGorjeta = int(input("Informe o percentual do servico entre 0 e 100: "))
        if percentualGorjeta < 0 or percentualGorjeta > 100:
            print("Valor invalido")
            break
        gorjeta = conta * (percentualGorjeta / 100)
        total = conta + gorjeta
        round(total,2)
        pagamento = total / pessoas
        round(pagamento, 2)
        print(f"O valor total da conta, com taxa de servico, sera de R$ {total}")
        print(f"\nDividindo a conta por {pessoas} pessoa(s), cada pessoa devera pagar R$ {pagamento}")
calculadoraGorjeta()