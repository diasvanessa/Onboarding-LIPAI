""" EX01 - Solicite ao usuário 3 notas e apresente o resultado da média aritmética. """

notas = []

for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média aritmética das notas é: {media}")

