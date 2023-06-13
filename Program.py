def fat(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * fat(i-1)

numero = int(input("Digite um número: "))
fatorial = fat(numero)
print(f"O fatorial do número {numero} é: {fatorial}")