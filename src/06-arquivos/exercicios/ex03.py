"""
Convertendo uma linha em dicionário genérico. Com base nos
códigos dos exercícios anteriores, crie a função:
def linha_para_dict(linha, chaves):
Recebe uma linha e uma lista de chaves e retorna um
dicionário.
...
 A função deve receber:
■ Uma linha do arquivo (string), por exemplo: SP000001,Maria da
Silva,maria@email.com
■ Uma lista de chaves, por exemplo: ['prontuario', 'nome', 'email']
■ Exemplo 1
● Linha: SP000001,Maria da Silva,maria@email.com
● Chaves: ['prontuario', 'nome', 'email']
● Saída:
{
'prontuario': 'SP000001',
'nome': 'Maria da Silva',
'email': 'maria@email.com'
}
■ Exemplo 2
● Linha: banana,3
● Chaves: ['item', 'quantidade']
● Saída:
{
'item': 'Banana',
'quantidade': '3'
}
■ Considere que todos os valores presentes no dicionário serão
strings (não é necessário converter para int/float neste
exercício, exceto quando explicitamente pedido em outros
enunciados, como no codigo de projeto no ex02).
■ Dica: esta função é genérica. Ela poderá ser reutilizada em
outros exercícios (como ex01 e ex02) para evitar duplicar
código
"""

def carregar_dados(nome_arquivo):
    lista_dicionarios = []
    lista_chaves = ["codigo", "titulo", "responsavel"]
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            dicionario = linha_para_dict(linha, lista_chaves)
            lista_dicionarios.append(dicionario)
    return lista_dicionarios


def linha_para_dict(linha, chaves):
    valores = linha.strip().split(sep=",")
    dicionario = {}
    contador = 0
    for chave in chaves:
        dicionario[chave] = valores[contador]
        contador += 1
    return dicionario

lista = carregar_dados("projetos.txt")
for dado in lista:
    print(dado)
