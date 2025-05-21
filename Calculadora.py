try:
    numero = int(input("Digite o número para ver a tabuada: "))
    limite = int(input("Multiplicar até qual número? "))

    print(f"\n Tabuada do {numero} até {limite}:")
    print("-" * 30)

    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado}")

    print("-" * 30)

except ValueError:
    print(" Por favor, digite apenas números inteiros.")