#Positivos e média
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())

count = 0
soma_positivos = 0

if A > 0:
    count = count + 1
    soma_positivos = soma_positivos + A
if B > 0:
    count = count + 1
    soma_positivos = soma_positivos + B
if C > 0:
    count = count + 1
    soma_positivos = soma_positivos + C
if D > 0:
    count = count + 1
    soma_positivos = soma_positivos + D
if E > 0:
    count = count + 1
    soma_positivos = soma_positivos + E
if F > 0:
    count = count + 1
    soma_positivos = soma_positivos + F

media = float(soma_positivos/count)

print(f'{count} valores positivos')
print('{0:.1f}'.format(media))