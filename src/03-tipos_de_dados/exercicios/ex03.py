"""
EX03
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída
Março).
○ Implementar usando um Dicionário (dict)
"""

MESES_ANO = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}

mes = int(input("Digite o mes do ano em formato numerico: "))

if mes in MESES_ANO:
    print(f'O mes correspondente eh: {MESES_ANO[mes]}')
else:
    print('Digite um numero correto!')
