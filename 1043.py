#Triangulo
import math
A,B,C=list(map(float,input().split()))
somaAB = A + B
somaBC = B + C
somaAC = A + C
subAB = math.fabs(A-B)
subAC = math.fabs(A-C)
subBC = math.fabs(B-C)

def perimetro(A,B,C):
    p = float(A + B + C)
    return p

def area(base,altura):
    a = float((base*altura)/2.0)
    return a
     
if A < somaBC and A > subBC:
    print('Perimetro = {0:.1f}'.format(perimetro(A,B,C)))          
elif B < somaAC and B > subAC:
    print('Perimetro = {0:.1f}'.format(perimetro(A,B,C)))         
elif C < somaAB and C > subAB:
    print('Perimetro = {0:.1f}'.format(perimetro(A,B,C)))
else:
    print('Area = {0:.1f}'.format(area(somaAB,C)))