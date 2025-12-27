"""
EX05
 Implemente uma calculadora de Índice de Massa Corporal (IMC)
usando as diretrizes da OMS. O programa deve:
○ Solicitar ao usuário seu peso (kg) e altura (m).
○ Calcular o IMC: 
■ IMC = peso / (altura * altura)
■ IMC Classificação
■ -----------------------------------
■ < 18,5 Baixo peso
■ 18,5 a 24,9 Peso normal
■ 25,0 a 29,9 Excesso de peso
■ 30,0 a 34,9 Obesidade de Classe 1
■ 35,0 a 39,9 Obesidade de Classe 2
■ >= 40,00 Obesidade de Classe 3
○ Apresentar também a situação atual do indivíduo em relação ao peso
normal: "normal" , "perder peso" , "ganhar peso"
○ Os dados do indivíduo devem ser organizados em um dicionário, por
exemplo:
individuo = {
'altura': 1.79,
'peso': 78.5
}
○ O programa deve ter, pelo menos, as seguintes funções:
def calcular_imc(individuo):
Retorna o IMC de um indivíduo com base na sua altura e peso.
pass
def obter_classificacao(imc):
Retorna a classificação com base no IMC.
pass
def situacao_individuo(imc):
Retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no
IMC.
pass
"""


def calcular_imc(individuo):
    peso = individuo['peso']
    altura = individuo['altura']
    if altura > 3:
        altura = altura / 100
    imc = peso / altura ** 2
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        return 'Baixo peso'
    elif 18.5 <= imc <= 24.9:
        return 'Peso normal'
    elif 25.0 <= imc <= 29.9:
        return 'Excesso de peso'
    elif 30.0 <= imc <= 34.9:
        return 'Obesidade de Classe 1'
    elif 35.0 <= imc <= 39.9:
        return 'Obesidade de Classe 2'
    else:  # imc >= 40
        return 'Obesidade de Classe 3'
    
def situacao_individuo(imc):
    return f'Sua situacao eh: {obter_classificacao(imc)} com base no imc de {imc:.2f}'


altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

individuo = {
    'altura': altura,
    'peso': peso
}

situacao = situacao_individuo(imc=(calcular_imc(individuo)))
print(situacao)