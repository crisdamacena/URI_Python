#Distância entre dois pontos
import math
valor1 = input().split()
valor2 = input().split()
eixox, eixoy = valor1
x1 = float(eixox)
y1 = float(eixoy)
eixox, eixoy = valor2
x2 = float(eixox)
y2 = float(eixoy)

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print('{0:.4f}'.format(distancia))