""" Aula 06 - Conversao de Tipos de Dados """


# Conversao de tipo implicita


leitura = 5.54

peso = 3

total = leitura * peso  # conversao implicita de int para float

print(total, type(total))  # 16.62 float


# Conversao de tipo explicita (type casting)


# soma = 13.4 + "7.2" TypeError


soma = 13.4 + float("7.2")  # converte string para float

print(soma, type(soma))  # 20.6 float

idade = "27"

print(idade, type(idade))  # 27 str

idade = int(idade) # converte string para int
print(idade, type(idade))  # 27 int

nome = "Vanessa"
altura = 1.58

# mensagem = nome + " tem a altura de " +  str(altura) converte float para string
# print(mensagem)  

mensagem = f"{nome} tem a altura de {altura}"  # f-string - converte automaticamente para string
print(mensagem)  

