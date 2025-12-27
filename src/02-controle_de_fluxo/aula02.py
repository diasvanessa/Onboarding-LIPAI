""" Aula 02.02 - instrucao if """

# if condicao:
#    instrucao
#    instrucao
#    instrucao

codigo_cliente = 32
desconto = 30.0
DESCONTO_ESPECIAL = desconto >= 20.0

# identacao de 4 espacos - recomendacao pep8

if DESCONTO_ESPECIAL:
    print('Desconto Especial')
    print(codigo_cliente)
else:
    print('Sem Desconto Especial')
    
# Nome tem que ter pelo menos 3 caracteres

nome = 'Joao'

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome invalido, precisa ter pelo menos 3 caracteres')    
else:
    print('Nome valido')

NOME_VALIDO = len(nome) >= 3

if NOME_VALIDO:
    print('Nome valido')    
else:
    print('Nome invalido, precisa ter pelo menos 3 caracteres')

if not NOME_INVALIDO:
    print('Nome valido')
else:
    print('Nome invalido, precisa ter pelo menos 3 caracteres')
    
# Nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
#exibir todos os erros no final apenas

nome = 'Joa'
idade = 16
erros = []
    
NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome invalido, precisa ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade invalida, precisa ser maior ou igual a 18 anos')
    

# False: False, None, 0, string vazia '', lista, tuple, set vazio, 0.0
# True: todo o resto    
    
if erros: # se a lista nao estiver vazia
    print(erros)
else:
    print('Dados validos')    
      
# if elif else

# Verifica se um numero eh positivo ou negativo ou zero

numero = -3

if numero > 0:
    print('Numero positivo')
elif numero < 0:
    print('Numero negativo')    
else:
    print('Zero')

# calcule a media e verifique se as duas notas 
# sao validas antes do calculo

nota1 = 5.6
nota2 = 10.0

# cuidado com ifs aninhados
if (nota1 >= 0.0 and nota1 <= 10.0) and (nota2 >= 0.0 and nota2 <= 10.0):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print('Aprovado com media:', media)
    elif media >= 4:
        print('Recuperacao com media:', media)
    else:
        print('Reprovado com media:', media)
else:
    print('Notas invalidas')
    
NOTA1_VALIDA = 0.0 <= nota1 <= 10.0
NOTA2_VALIDA = 0.0 <= nota2 <= 10.0
    
if NOTA2_VALIDA and NOTA1_VALIDA:
    media = (nota1 + nota2) / 2
    if media >= 6:
        print('Aprovado com media:', media)
    elif media >= 4:
        print('Recuperacao com media:', media)
    else:
        print('Reprovado com media:', media)
else:
    print('Notas invalidas')