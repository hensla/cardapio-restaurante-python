print("Lanche: 1")
print("Bebida: 2")
print("Sobremesa: 3")
print("Sair: 4")

opc = int(input("digite uma opção: "))

match opc:
    case 1:
        print("1.Cachorro-quente R$ 20")
        print("2.Hamburguer R$ 30")

        numeroDoLanche = int(input("Insira o numero do lanche: "))
        if numeroDoLanche == 1:
            hd = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {20 * hd:.2f}")
        elif numeroDoLanche == 2:
            h = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {30 * h:.2f}")

    case 2:
        print("1. Refrigerante R$ 8")
        print("2. Suco R$ 6")

        numeroDoLanche = int(input("Insira o numero do lanche: "))
        if numeroDoLanche == 1:
            rf = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {8 * rf:.2f}")
        elif numeroDoLanche == 2:
            sc = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {6 * sc:.2f}")

    case 3:
        print("1. Sorvete R$ 10")
        print("2. Bolo R$ 15")

        numeroDoLanche = int(input("Insira o numero do lanche: "))
        if numeroDoLanche == 1:
            svt = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {10 * svt:.2f}")
        elif numeroDoLanche == 2:
            bl = int(input("Quantos você deseja? "))
            print(f"O valor total deu: R$ {15 * bl:.2f}")

    case 4:
        print("Obrigado, volte sempre. :)")