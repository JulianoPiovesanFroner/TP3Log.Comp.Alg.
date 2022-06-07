def verificadorIdade():
    while True:
        idade = int(input("Informe a idade: "))
        if idade < 0:
            print("Idade invalida")
            break
        elif idade >= 18 and idade <= 70:
            print("Tem obrigacao de votar.")
        elif (idade > 16 and idade < 18) or idade > 70:
            print("Nao tem obrigacao de votar.")
        else:
            print("Nao tem direito ao voto.")
verificadorIdade()