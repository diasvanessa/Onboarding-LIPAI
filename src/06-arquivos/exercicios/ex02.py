"""
ex02.py – Carregar dados de projetos. Implemente a função:
def carregar_dados_projetos(nome_arquivo):
Retorna uma tupla de dicionários com dados de
projetos.
...
○ A função deve:
■ Receber como parâmetro o nome de um arquivo que contém
dados de projetos.
■ Retornar uma tupla, onde cada elemento é um dicionário com
as chaves:
● codigo – número inteiro que representa o código do
projeto
● titulo
● responsavel – nome do responsável pelo projeto
○ Assim como no exercício anterior, não utilize bibliotecas prontas para
leitura e parse do arquivo; implemente a lógica de divisão da linha em
campo

"""

def carregar_dados_projetos(nome_arquivo):
    """Retorna uma tupla de dicionários com dados de
    projetos."""
    projetos = []    
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            codigo, titulo, responsavel = linha.split(sep=",")
            codigo = int(codigo)
            projeto = {
                "codigo": codigo,
                "titulo": titulo,
                "responsavel": responsavel
            }
            projetos.append(projeto)
    return tuple(projetos)
    
projetos = carregar_dados_projetos("projetos.txt")
for projeto in projetos:
    print(projeto)