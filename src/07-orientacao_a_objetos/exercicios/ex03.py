"""
ex03.py – Classe Participacao
○ Implemente uma classe Participacao com os seguintes atributos:
■ codigo – identificador da participação (pode ser inteiro ou
string, você escolhe, mas seja consistente)
■ data_inicio
■ data_fim
■ aluno – um objeto da classe Aluno
■ projeto – um objeto da classe Projeto associado
○ Você pode começar armazenando as datas como strings (ex:
"2025-03-01"). Em atividades futuras, podemos trabalhar com tipos de
data mais específicos.
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
     

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("O código da participação não pode ser vazio.")
        self._codigo = codigo

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        if not isinstance(data_inicio, str) or not data_inicio.strip():
            raise ValueError("A data de início deve ser uma string não vazia.")
        self._data_inicio = data_inicio

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        if not isinstance(data_fim, str) or not data_fim.strip():
            raise ValueError("A data de fim deve ser uma string não vazia.")
        self._data_fim = data_fim

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("Aluno deve ser um objeto da classe Aluno.")
        self._aluno = aluno

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, projeto):
        if not isinstance(projeto, Projeto):
            raise ValueError("Projeto deve ser um objeto da classe Projeto.")
        self._projeto = projeto

    def __str__(self):
        return (
            f"Participacao[codigo={self.codigo}, "
            f"data_inicio={self.data_inicio}, "
            f"data_fim={self.data_fim}, "
            f"aluno={self.aluno.prontuario}, "
            f"projeto={self.projeto.codigo}]"
        )
        
aluno = Aluno("SP000002","Pedro Gomes","pedro@email.com")
projeto = Projeto("1003","Plataforma de Ensino a Distância","Mariana Souza")

participacao = Participacao("100", "20-02-2025", "20-08-2025", aluno, projeto)

print(participacao)