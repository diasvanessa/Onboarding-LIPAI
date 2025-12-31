"""
ex01.py – Classe Aluno
○ Implemente uma classe Aluno com:
■ Atributos:
● prontuario
● nome
● email
■ Requisitos:
● Deve ser possível construir um objeto Aluno a partir de
uma string no formato: "prontuario,nome,email"
Exemplo: "SP0101,João da Silva, joao@email.com"
● Nenhum dos atributos pode ser vazio ou nulo.
● Use propriedades (@property e setters) para validar os
valores.
● Dois alunos devem ser considerados iguais se tiverem o
mesmo prontuário.
● Implemente o método especial __eq__ para comparar
objetos Aluno por prontuário.

● (Opcional, mas recomendado) Considere também
implementar __hash__ se quiser usar alunos em
conjuntos (set) ou como chaves de dicionário.
"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, prontuario):
        if not prontuario:
            raise ValueError("O prontuario não pode ser vazio.")
        self ._prontuario = prontuario
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("O email não pode ser vazio.")
        self._email = email
    
    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=",")
        return cls(prontuario, nome, email)
    
    def __hash__(self):
        return hash(self.prontuario)
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False
    
    def __str__(self):
        return f"Aluno[prontuario = {self.prontuario}, nome= {self.nome}, email= {self.email}]"
    
string1 = "SP0101,João da Silva, joao@email.com"
string2 = "SP0102, Maria da Silva, maria@email.com"    
    
aluno1 = Aluno.from_string(string1)
aluno2 = Aluno.from_string(string2)
aluno3 = Aluno("SP000002","Pedro Gomes","pedro@email.com")

print(aluno1)
print(aluno2)
print(aluno3)