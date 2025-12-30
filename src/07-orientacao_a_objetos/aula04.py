""" Aula 07.04 – Propriedades """

# formas de controlar acesso aos atributos de uma intancia
# formas personalizadas em obter e alterar o valor de um atributo

class Retangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    # getter    
    @property # decorar com propriedade
    def base(self):
        return self._base 
    
    # setter
    @base.setter
    def base(self, value):
        if value <= 0:
            raise ValueError('A base deve ser maior que 0')
        self._base = value
           
    @property 
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, value):
        if value <= 0:
            raise ValueError('A altura deve ser maior que 0')
        self._altura = value

    # metodos associados a instancia
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    @classmethod # metodo de classe e nao de instancia
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))
    
retangulo1 = Retangulo(10.0, 5.0)

# retangulo1.base = -3.0
print(retangulo1.base, retangulo1.altura)