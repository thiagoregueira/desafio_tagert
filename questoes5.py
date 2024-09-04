def inverter_palavra(palavra):
    palavra_invertida = ''
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
    return palavra_invertida


def main():
    palavra = input('Digite uma palavra:\n')

    palavra_invertida = inverter_palavra(palavra)

    print(f'A palavra invertida é: {palavra_invertida}')


if __name__ == '__main__':
    main()
