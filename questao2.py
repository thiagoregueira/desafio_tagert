def sequencia_fibo(limit):
    sequencia = [0, 1]
    while sequencia[-1] < limit:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return sequencia


def faz_parte_da_sequencia_fibo(valor):
    sequencia = sequencia_fibo(valor)
    return valor in sequencia


def main():
    valor = int(input('Digite um valor:\n'))

    if faz_parte_da_sequencia_fibo(valor):
        print(f'O valor {valor} faz parte da sequência de Fibonacci.')
    else:
        print(f'O valor {valor} não faz parte da sequência de Fibonacci.')


if __name__ == '__main__':
    main()
