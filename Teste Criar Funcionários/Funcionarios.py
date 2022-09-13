class ExceptionTurno(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

class ExceptionMinSalario(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

class Funcionario:

    __SALARIO_MINIMO = 1200.00

    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario

    def add_aumento(self, valor):
        self.aumento = self.salario + valor
        return self.aumento

    def ganho_anual(self):
        self.total_ano = self.salario * 13
        return self.total_ano

    def exibe_dados(self):
        return f"O Funcionário {self.nome} recebe {self.salario} e ganha anualmente {self.ganho_anual()}\n"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,salario):
        self.__salario = salario
    
class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula) -> None:
        super().__init__(nome, salario)
        self.matricula = matricula

        def exibe_dados(self):
            return super().exibe_dados()

        @property
        def matricula(self):
            return self.__matricula

        @matricula.setter
        def matricula(self, matricula):
            self.__matricula = matricula

class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus) -> None:
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def ganho_anual(self):
        return super().ganho_anual() + self.bonus * 12

class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno) -> None:
        super().__init__(nome, salario, matricula)
        self.turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    def ganho_anual(self):
        self.adicional_noturno = 150 * 12
        return super().ganho_anual() + self.adicional_noturno

    def exibe_dados(self):
        return super().exibe_dados() + (f'Turno: {self.turno}')