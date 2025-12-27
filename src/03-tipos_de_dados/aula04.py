""" Aula 03.04 – Dicionários(Dics) """

# colecao de key-value (chave-valor)
# valores indexaveis pela chave unica
# mutavel

# criar um dict

carro = {
    'marca': 'Ford',  # chave: valor
    'modelo': 'Mustang',
    'ano': 1964
}

print(carro, type(carro))

# acessar valores por chave
print(carro['marca'])
print(carro.get('marca'))

# pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())  # lista de tuplas

# verifica se chave existe
print('marca' in carro)

# adicionar chave/valor de forma dinamica
carro['cor'] = 'Vermelho'
print('cor' in carro)
print(carro, type(carro))

# remover item do dicionario
carro.pop('marca')
print(carro, type(carro))

# loop
# for key in carro:
#     print(key, carro[key], type(key))

# for value in carro.values():
#     print(value)

# for key in carro.keys():
#     print(key)

for key, value in carro.items():
    print(key, value)

# lista de dicionarios

aluno1 = {
    'nome': 'Joao',
    'email': 'joao@mail.com',
    'notas': [10.0, 5.5, 2.0]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@mail.com',
    'notas': [10.0, 8.5, 9.0]
}

alunos = [aluno1, aluno2]
for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)
