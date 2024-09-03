import json

with open('D3.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = [dia["valor"] for dia in dados if dia["valor"] > 0]

min_faturamento = min(faturamento_diario)

max_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_na_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor faturamento: R$ {min_faturamento:.2f}")
print(f"Maior faturamento: R$ {max_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_na_media} dias")

