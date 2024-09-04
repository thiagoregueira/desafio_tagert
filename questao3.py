import json


def calcular_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)

    faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

    if not faturamento_diario:
        return 'Ainda não houve faturamento'

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_da_media = sum(
        1 for faturamento in faturamento_diario if faturamento > media_mensal
    )

    return menor_faturamento, maior_faturamento, dias_acima_da_media


# Exemplo


caminho_arquivo = 'dados.json'
menor_faturamento, maior_faturamento, dias_acima_da_media = (
    calcular_faturamento(caminho_arquivo)
)


print(f'Menor faturamento: R$ {menor_faturamento}')
print(f'Maior faturamento: R$ {maior_faturamento}')
print(f'Dias acima da média: {dias_acima_da_media}')
