while True:
    nome1 = input("Informe o nome do 1 participante: ")
    nota1 = float(input("Informe a nota do 1 participante: "))
    if not nota1 >= 0 or not nota1 <= 10:
        print("Valor invalido.")
        break

    nome2 = input("Informe o nome do 2 participante: ")
    nota2 = float(input("Informe a nota do 2 participante: "))
    if not nota2 >= 0 or not nota2 <= 10:
        print("Valor invalido.")
        break

    nome3 = input("Informe o nome do 3 participante: ")
    nota3 = float(input("Informe a nota do 3 participante: "))
    if not nota3 >= 0 or not nota3 <= 10:
        print("Valor invalido.")
        break

    nome4 = input("Informe o nome do 4 participante: ")
    nota4 = float(input("Informe a nota do 4 participante: "))
    if not nota4 >= 0 or not nota4 <= 10:
        print("Valor invalido.")
        break

    nome5 = input("Informe o nome do 5 participante: ")
    nota5 = float(input("Informe a nota do 5 participante: "))
    if not nota5 >= 0 or not nota5 <= 10:
        print("Valor invalido.")
        break

    notas = [nota1,nota2,nota3,nota4,nota5]
    notas.sort(reverse=True)
    notaVencedor = notas[0]

    participantes = {
        nome1: nota1,
        nome2: nota2,
        nome3: nota3,
        nome4: nota4,
        nome5: nota5
        }

    nomes = list(participantes.keys())
    notas = list(participantes.values())
    
    posicaoVencedor = notas.index(notaVencedor)
    vencedor = nomes[posicaoVencedor]

    print(f"\nO(a) vencedor(a) foi {vencedor} com nota {notaVencedor}!\n")
    if input("Digite 's' para sair ou enter para comecar de novo: ") == "s":
        break