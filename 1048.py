#Aumento de salário
salario = eval(format(float(input()), '.2f'))
percentual = float(0.0)

def aumento(salario, acrescimo):
    novosalario = salario + acrescimo
    return novosalario

def valoraumento(salario, reajuste):
    acrescimo = salario*reajuste
    return acrescimo


if salario > 0 and salario <= 400.00:
    acrescimo = valoraumento(salario, 0.15)
    valorfinal = aumento(salario, acrescimo)
    percentual = 15    
elif salario >= 400.01 and salario <= 800.00:
    acrescimo = valoraumento(salario, 0.12)
    valorfinal = aumento(salario, acrescimo)
    percentual = 12
elif salario >= 800.01 and salario <= 1200.00:
    acrescimo = valoraumento(salario, 0.1)
    valorfinal = aumento(salario, acrescimo)
    percentual = 10
elif salario > 1200.01 and salario <= 2000.00:
    acrescimo = valoraumento(salario, 0.07)
    valorfinal = aumento(salario, acrescimo)
    percentual = 7
elif salario > 2000.00:
    acrescimo = valoraumento(salario, 0.04)
    valorfinal = aumento(salario, acrescimo)
    percentual = 4
    
print('Novo salario: {0:.2f}'.format(valorfinal))
print('Reajuste ganho: {0:.2f}'.format(acrescimo))
print('Em percentual: {} %'.format(percentual))