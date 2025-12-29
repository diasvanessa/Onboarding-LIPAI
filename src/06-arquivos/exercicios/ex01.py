"""
ex01.py – Carregar dados de alunos. Implemente a função:
def carregar_dados_alunos(nome_arquivo):
Retorna uma tupla de dicionários com dados de
alunos.
 A função deve:
■ Receber como parâmetro o nome de um arquivo que contém
dados de alunos.
■ Ler o arquivo linha a linha.
■ Para cada linha, criar um dicionário com as chaves:
● prontuario
● nome
● email

■ Retornar uma tupla, onde cada elemento é um dicionário com
os dados de um aluno.
■ Exemplo de arquivo de dados (texto):
SP000001,Maria da Silva,maria@email.com
SP000002,Pedro Gomes,pedro@email.com
SP000003,João Santos,joao@email.com
● Desenvolva a lógica de leitura e processamento “na mão”.
● Não utilize bibliotecas como csv ou pandas para fazer a leitura pronta
do arquivo; implemente você mesmo a separação dos campos a partir
da string da linha.
"""

def carregar_dados_alunos(nome_arquivo):
    """Retorna uma tupla de dicionarios com dados de alunos."""
    alunos = []
    
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip() # retira caracter no final
            codigo, nome, email = linha.split(sep=",") # quebra em pedacos
            aluno = {
                "prontuario": codigo,
                "nome": nome,
                "email": email
            }
            alunos.append(aluno)

    return tuple(alunos) # converte a lsita em tupla

# breakpoint()
alunos = carregar_dados_alunos("alunos.txt")
print(alunos)