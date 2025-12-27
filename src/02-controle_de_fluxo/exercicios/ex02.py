""" solicite ao usuário, uma única vez, as notas no formato n1, n2, n3,
nm e apresente:
○ a média aritmética das notas;
○ a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou
reprovado (média < 4.0).
○ Dicas:
■ Use o método split da classe str para obter uma lista de notas.
■ O programa deve funcionar para qualquer quantidade de notas
(ex.: 10.0, 3.0 ou 10.0, 3.0, 2.0, 5.6, 8.2). """

notas_input = input(
    "Digite as notas separadas por vírgula (ex.: 10.0, 3.0, 5.5): ")
notas_str = notas_input.split(',')
notas_float = []

for nota in notas_str:
    notas_float.append(float(nota.strip()))

print(notas_float)

soma = 0
for nota in notas_float:
    soma += nota
    
media = soma / len(notas_float)

ALUNO_APROVADO = media > 6.0
ALUNO_RECUPERACAO = 4.0 <= media <= 6.0
situacao = ''

if ALUNO_APROVADO:
    situacao = 'Aprovado'
elif ALUNO_RECUPERACAO:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'    
    
print(f"Média: {media:.2f} - Situação: {situacao}")
