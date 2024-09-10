# 3) Dado um vetor que guarda o valor de faturamento diário de uma 
# distribuidora, faça um programa, na linguagem que desejar, que 
# calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi 
# superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e 
# feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Carrega os dados do arquivo JSON
with open('dados.json', 'r') as f:
    dados = json.load(f)

# Remove os dias com faturamento zero
faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcula a média mensal de faturamento
media_mensal = sum(faturamentos) / len(faturamentos)

# Conta o número de dias com faturamento superior à média
dias_acima_media = len([valor for valor in faturamentos if valor > media_mensal])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
