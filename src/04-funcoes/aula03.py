""" Aula 03 - Entendendo o 
uso de *args e **kwargs em funções e métodos """

print('*args: ')

# iteracao sobre os elementos passados

def world_cup_titles(country, *args):    
    print('Country: ', country)
    for title in args:
        print('year: ', title)
        
world_cups = {
    "Brasil": [1958, 1962, 1970, 1994, 2002],
    "Alemanha": [1954, 1974, 1990, 2014],
    "Itália": [1934, 1938, 1982, 2006],
    "Argentina": [1978, 1986, 2022],
    "França": [1998, 2018]
}

for country, titles in world_cups.items():
    world_cup_titles(country, *titles)
    
print('\n **kwargs')

# os argumentos sao opicionais com finalidades diferentes, 
# precisam ser identificadas pelo nome

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')    
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount    
    return value

final_price = calculate_price(100.0)
print(final_price)

final_price = calculate_price(100.0, discount=5.0)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)