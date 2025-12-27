"""
EX 06
Crie um programa em Python que recebe como entrada o
comprimento, altura e largura (em cm) de um aquário e calcule:
○ O volume do aquário em litros;
○ A potência do termostato necessária para manter a temperatura adequada

○ A quantidade de filtragem por hora (em litros) necessária para manter a
qualidade da água.
● Volume (L) = (comprimento * altura * largura) / 1000
● Potência do termostato: = volume * 0.05 * (temperatura_desejada -
temperatura_ambiente)
● Filtragem por hora: deve ser no mínimo de 2 a 3 vezes o volume do aquário.
● Requisitos:
○ Definir uma estrutura de dados para representar as entradas do usuário (por
exemplo, um dicionário com medidas e temperaturas).
○ Criar funções separadas para:
■ calcular o volume;
■ calcular a potência do termostato;
■ calcular a faixa mínima e máxima de filtragem recomendada.
○ Apresentar os resultados finais de forma organizada para o usuário.

"""

def calcular_volume(aquario):
    comprimento = aquario['comprimento']
    altura = aquario['altura']
    largura = aquario['largura']
    return (comprimento*altura*largura) / 1000

def potencia_termostato(aquario, volume):
    temperatura_ambiente = aquario['temperatura_ambiente']
    temperatura_desejada = aquario['temperatura_desejada']
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia    
    
def filtragem_recomendada(volume):
    faixa_min = 2 * volume
    faixa_max = 3 * volume
    faixas = [faixa_min, faixa_max]
    return faixas
    

comprimento = float(input('Digite o comprimento do aquario em centimetros: '))
altura = float(input('Digite a altura do aquario em centimetros: '))
largura = float(input('Digite a largura do aquario em centimetros: '))
temperatura_desejada = float(input('Digite a temperatura desejada: '))
temperatura_ambiente = float(input('Digite a temperatura ambiente: '))

input_aquario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temperatura_desejada': temperatura_desejada,
    'temperatura_ambiente': temperatura_ambiente
}

vol_aquario = calcular_volume(input_aquario)
print(f'O volume desse aquario eh de: {vol_aquario} litros')
print(f'A potencia do termostato necessaria para manter a temperaturaadequada eh de: {potencia_termostato(input_aquario, vol_aquario)}')

faixa = filtragem_recomendada(vol_aquario)

print(f'A faixa minima de filtragem recomendada eh de {faixa[0]} e a maxima eh de {faixa[1]}')

