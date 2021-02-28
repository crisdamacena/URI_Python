#Área
entrada =input().split()

valor1, valor2, valor3 = entrada
A = float(valor1)
B = float(valor2)
C = float(valor3)

def triangulo(A,C):
    area = float((A*C)/2)
    return area

def circulo(C):
    pi = 3.14159
    area = float(pi*(C**2))
    return area

def trapezio(A,B,C):
    area = float(((A+B)*C)/2)
    return area

def quadrado(B):
    area = float(B**2)
    return area

def retangulo(A,B):
    area = float(A*B)
    return area    
        
print('TRIANGULO: {0:.3f}'.format(triangulo(A,C)))
print('CIRCULO: {0:.3f}'.format(circulo(C)))
print('TRAPEZIO: {0:.3f}'.format(trapezio(A,B,C)))
print('QUADRADO: {0:.3f}'.format(quadrado(B)))
print('RETANGULO: {0:.3f}'.format(retangulo(A,B)))

