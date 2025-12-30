""" Aula 07.05 – Métodos especiais """ 
# __str__(self)
# representacao do obejto como string para humanos

# __repr__(self)
# representacao do objeto como string para recriar esse obj
# logging, debug
# representacao canonica

class Retangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f'Retangulo[base = {self.base}, altura = {self.altura}]'
    
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'
    
    
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 14.0)

representacao_string_retangulo = 'Retangulo(7.5,12.3)'
print(retangulo1.__repr__)

retangulo3 = eval(representacao_string_retangulo)
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)