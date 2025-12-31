"""
ex02.py – Classe Projeto
○ Implemente uma classe Projeto com:
■ Atributos:
● codigo – número inteiro que representa o código do
projeto
● titulo
● responsavel – nome do professor responsável pelo
projeto
■ Requisitos:
● Deve ser possível construir um objeto projeto a partir de
uma string no formato: "codigo,titulo,responsavel"
Exemplo: "1,Laboratório de Desenvolvimento de
Software,Pedro Gomes"
● Nenhum dos atributos pode ser vazio ou nulo (use
propriedades).
● O atributo codigo deve ser armazenado como inteiro.
● Dois projetos devem ser considerados iguais se tiverem
o mesmo código (codigo).
● Implemente __eq__ comparando pelo código.
"""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            if not codigo.isdigit():
                raise ValueError("O código deve conter apenas números.")
            codigo = int(codigo)

        if not isinstance(codigo, int):
            raise ValueError("O código do projeto deve ser um inteiro.")

        if codigo <= 0:
            raise ValueError("O código deve ser positivo.")

        self._codigo = codigo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if not titulo or not str(titulo).strip():
            raise ValueError("O título do projeto não pode ser vazio.")
        self._titulo = titulo

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, responsavel):
        if responsavel is None:
            raise ValueError("O responsável pelo projeto não pode ser nulo.")
        self._responsavel = responsavel
        
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return value.codigo == self.codigo   
        return False    
    
    def __str__(self):
        return f"Projeto[codigo = {self.codigo}, titulo= {self.titulo}, responsavel= {self.responsavel}]"
    
projeto1 = Projeto("1001","Sistema de Gestão Escolar","Ana Paula Ribeiro")
projeto2 = Projeto("1002","Aplicativo de Controle Financeiro","Carlos Eduardo Lima")
projeto3 = Projeto("1003","Plataforma de Ensino a Distância","Mariana Souza")

print(projeto1)
print(projeto2)
print(projeto3)