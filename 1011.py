#Esfera
def potencia(n, k):
    pot = 1
    i   = 0
    while i < k:
        pot = pot * n
        i   = i + 1
    return pot

raio = float(input())
pi = 3.14159

raiocubo = potencia(raio, 3)
volume = (4.0/3.0) * pi * (raio*raio*raio)

print('VOLUME = {0:.3f}'.format(volume))