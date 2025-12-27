"""
EX 02 
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída
Março).
○ Implementar usando uma Tupla (tuple).
"""

MESES_ANO = (
    'Janeiro',
    'Fevereiro',
    'Marco',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
)

mes = int(input("Digite o mes do ano em formato numerico: "))

if 1 <= mes <= 12:
    print(f'Mes correspondente: {MESES_ANO[(mes-1)]}')
else:
    print('Digite um numero entre 1 e 12!')

