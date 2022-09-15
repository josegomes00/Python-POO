from Classes import *

SALARIO_PRESIDENTE = 2500
SALARIO_GERENTE = 3500
SALARIO_DIRETOR = 5000

#Coletando Dados do Funcionário#

#NOME#
print("     CADASTRO DE FUNCIONÁRIO")
name = input("DIGITE O NOME DO FUNCIONÁRIO: ")
name = name.upper()

#NÍVEL DE FORMAÇÃO#
print("\nNível de Formação\n\nMÉDIO COMPLETO[1]\nSUPERIOR COMPLETO[2]\nESPECIALIZADO[3]\nMESTRADO COMPLETO[4]\nDOUTORADO COMPLETO[5]\n")
formacao = int(input())

if formacao == 1:
    formacao = GrauInstrucao.MEDIO

elif formacao == 2:
    formacao = GrauInstrucao.SUPERIOR

elif formacao == 3:
    formacao = GrauInstrucao.ESPECIALISTA

elif formacao == 4:
    formacao = GrauInstrucao.MESTRE

elif formacao == 5:
    formacao = GrauInstrucao.DOUTOR

#CARGO#
print("\n       CARGO NA EMPRESA")
print("\nPRESIDENTE[1]\nGERENTE[2]\nDIRETOR[3]\n")
cargo = int(input())

#MONTANDO FUNCIONÁRIO#

if cargo == 1:
    f = Presidente(name,SALARIO_PRESIDENTE,formacao)           
elif cargo == 2:
    f = Gerente(name,SALARIO_GERENTE,formacao)
elif cargo == 3:
    f = Diretor(name,SALARIO_DIRETOR,formacao)

print(f)
