""" EX04 - baseado no ex03.py, ao final do programa apresente todas as
inconsistências do identificador informado (use uma list de erros).
Exemplos:
○ Entrada: B9999999X
■ Erros:
● O identificador não inicia com a sequência BR.
● O identificador não apresenta número inteiro entre 0001
e 9999.
○ Entrada: BR9999Y
■ Erros:
● O identificador não finaliza com o caractere X
"""

identificador = input('Digite o identificador: ')

erros = []

INICIO_VALIDO = identificador.startswith('BR')
if INICIO_VALIDO is False:
    erros.append('O identificador nao inicia com a sequência BR.')

TAMANHO_VALIDO = len(identificador) == 7
if TAMANHO_VALIDO is False:
    erros.append('O identificador deve ter exatamente 7 caracteres.')
    
NUMERO_VALIDO = False
if TAMANHO_VALIDO:
    numero_str = identificador[2:6]
    if numero_str.isdigit():
        numero = int(numero_str)
        if 1 <= numero <= 9999:
            NUMERO_VALIDO = True
if NUMERO_VALIDO is False:
    erros.append('O identificador nao apresenta numero inteiro entre 0001 e 9999.')

FIM_VALIDO = identificador.endswith('X')
if FIM_VALIDO is False:
    erros.append('O identificador nao finaliza com o caractere X.')
    
if erros:
    print('Erros:')
    for erro in erros:
        print(f'● {erro}')
else:
    print('Identificador válido!')
