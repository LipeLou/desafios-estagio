'''
3) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''

# Faturamento mensal por estado
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def percentual_estados(faturamento):
    # Armazendando o faturamento total
    faturamento_total = sum(faturamento.values())

    # Dict comprehension - {chave: valor for item in lista}
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

percentual_estados(faturamento_mensal)