fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

fat_total = sum(fat.values())

for estado, valor in fat.items():
    percentual = (valor / fat_total) * 100
    print(f"{estado}: {percentual:.2f}% do faturamento total")
