#Formula de baskara
import math
entrada = input().split()
valor1, valor2, valor3 = entrada
A = float(valor1)
B = float(valor2)
C = float(valor3)

def baskara(A,B,C):
    delta = float((B**2) - 4*A*C)
    if A == 0:
        print('Impossivel calcular')
        exit()
    if delta < 0:
        print('Impossivel calcular')
        exit()
    else:
        raizdelta = math.sqrt(delta)
        R1 = float(((-B) + raizdelta)/(2*A))
        R2 = float(((-B) - raizdelta)/(2*A))
        print('R1 = {0:.5f}'.format(R1))
        print('R2 = {0:.5f}'.format(R2))

baskara(A,B,C)