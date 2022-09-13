from abc import ABC, abstractmethod
from enum import Enum

class GrauInstrucao(Enum):
    MEDIO = "Medio"
    SUPERIOR = "Superior"
    ESPECIALISTA = "Especialista"
    MESTRE = "Mestre"
    DOUTOR = "DOUTOR"

    def __str__(self):
        return self.value

class Funcionario(ABC):

    def __init__(self, nome, salario, instrucao):
        super().__init__()
        self.nome = nome
        self.salario = salario
        self.instrucao = instrucao
        self._bonificacao = 0.0
        self.addbonificacao()

    @abstractmethod
    def addbonificacao(self):
        pass

    def contracheque(self):
        return self.__salario + self._bonificacao

    def __str__(self):
        return f"Cargo: {type(self).__name__}\nNOME: {self.__nome}\nSalário Total: {self.contracheque():.2f}"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, f'O Nome do {type(self).__name__} deve ser em LETRAS'
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        assert type(salario) == int or type(salario), 'Salário deve ser numérico'
        assert salario > 0, f'Salário de {self.__nome} deve ser maior que 0'
        self.__salario = salario

    @property
    def instrucao(self):
        return self.__instrucao

    @instrucao.setter
    def instrucao(self, instrucao):
        assert type(instrucao) == GrauInstrucao, "Grau Instrução deve ser do tipo ENUM."
        self.__instrucao = instrucao

    @property
    def bonificacao(self):
        return self._bonificacao

class Presidente(Funcionario):
    def __init__(self, nome, salario, instrucao):
        super().__init__(nome, salario, instrucao)
        
    def addbonificacao(self):      
        if self.instrucao == GrauInstrucao.DOUTOR:
            self._bonificacao = self.salario * 4
            
        else:
            self._bonificacao = self.salario * 2
            
    def contracheque(self):
        return super().contracheque()
      
class Gerente(Funcionario):
    def __init__(self, nome, salario, instrucao):
        super().__init__(nome, salario, instrucao)
        
    def addbonificacao(self):
        if self.instrucao == GrauInstrucao.ESPECIALISTA:
            self._bonificacao = self.salario * 0.15
            
        elif self.instrucao == GrauInstrucao.MESTRE:
            self._bonificacao = self.salario * 0.25
            
        elif self.instrucao == GrauInstrucao.DOUTOR:
            self._bonificacao = self.salario * 0.5
            
    def contracheque(self):
        return super().contracheque()
    
class Diretor(Gerente):
    def __init__(self, nome, salario, instrucao):
        super().__init__(nome, salario, instrucao)
        
    def addbonificacao(self):
        super().addbonificacao()
        self._bonificacao += self.salario * 0.3