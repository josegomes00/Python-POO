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
while True:
    print("\nNível de Formação\n\nMÉDIO COMPLETO[1]\nSUPERIOR COMPLETO[2]\nESPECIALIZADO[3]\nMESTRADO COMPLETO[4]\nDOUTORADO COMPLETO[5]\n")
    try:
        formacao = int(input())
        
        if formacao == 1:
            formacao = GrauInstrucao.MEDIO
            break
        elif formacao == 2:
            formacao = GrauInstrucao.SUPERIOR
            break
        elif formacao == 3:
            formacao = GrauInstrucao.ESPECIALISTA
            break
        elif formacao == 4:
            formacao = GrauInstrucao.MESTRE
            break
        elif formacao == 5:
            formacao = GrauInstrucao.DOUTOR
            break
        else:
            raise Exception
        
    except ValueError:
        print("Apenas Números.")
        
    except Exception:
        print("Opção Inválida.")
        
#CARGO#

while True:
    CARGOS_VALIDOS = [1,2,3]
    try:
        print("\n       CARGO NA EMPRESA")
        print("\nPRESIDENTE[1]\nGERENTE[2]\nDIRETOR[3]\n")
        cargo = int(input())
        if cargo not in CARGOS_VALIDOS:
            raise Exception
        break
    
    except ValueError:
        print("Apenas Números.")
        
    except:
        print("Opção Inválida.")

#MONTANDO FUNCIONÁRIO#

if cargo == 1:
    f = Presidente(name,SALARIO_PRESIDENTE,formacao)           
elif cargo == 2:
    f = Gerente(name,SALARIO_GERENTE,formacao)
elif cargo == 3:
    f = Diretor(name,SALARIO_DIRETOR,formacao)

print(f)
