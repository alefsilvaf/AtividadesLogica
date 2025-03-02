import json

with open("faturamento.json", "r") as file:
    dados = json.load(file)

valores = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
