def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

numero = int(input("Digite um número: "))

if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
