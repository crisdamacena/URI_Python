#Pares, ímpares, positivos e negativos
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())

contapar = 0
contaimpar = 0
contapositivo = 0
contanegativo = 0

def verificapar(n):
    if n%2 == 0:
        return 1
    else:
        return 0
    
def verificaimpar(n):
    if n%2 != 0:
        return 1
    else:
        return 0
    
def verificapositivo(n):
    if n > 0:
        return 1
    else:
        return 0
    
def verificanegativo(n):
    if n < 0:
        return 1
    else:
        return 0

contapar = contapar + verificapar(A)
contapar = contapar + verificapar(B)
contapar = contapar + verificapar(C)
contapar = contapar + verificapar(D)
contapar = contapar + verificapar(E)

contaimpar = contaimpar + verificaimpar(A)
contaimpar = contaimpar + verificaimpar(B)
contaimpar = contaimpar + verificaimpar(C)
contaimpar = contaimpar + verificaimpar(D)
contaimpar = contaimpar + verificaimpar(E)

contapositivo = contapositivo + verificapositivo(A)
contapositivo = contapositivo + verificapositivo(B)
contapositivo = contapositivo + verificapositivo(C)
contapositivo = contapositivo + verificapositivo(D)
contapositivo = contapositivo + verificapositivo(E)

contanegativo = contanegativo + verificanegativo(A)
contanegativo = contanegativo + verificanegativo(B)
contanegativo = contanegativo + verificanegativo(C)
contanegativo = contanegativo + verificanegativo(D)
contanegativo = contanegativo + verificanegativo(E)

print(f'{contapar} valor(es) par(es)')
print(f'{contaimpar} valor(es) impar(es)')
print(f'{contapositivo} valor(es) positivo(s)')
print(f'{contanegativo} valor(es) negativo(s)')