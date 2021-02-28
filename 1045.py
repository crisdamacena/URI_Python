#Tipos de Triangulos
A,B,C=list(map(float,input().split()))
lista = [A,B,C]
lista.sort(reverse=True)

ladomaior = lista[0]
somaBC = lista[1]+lista[2]
quadradoA = lista[0]**2
quadradoB = lista[1]**2
quadradoC = lista[2]**2

if ladomaior >= somaBC:
    print('NAO FORMA TRIANGULO')
else:
    if quadradoA == (quadradoB + quadradoC):
        print('TRIANGULO RETANGULO')
    if quadradoA > (quadradoB + quadradoC):
        print('TRIANGULO OBTUSANGULO')
    if quadradoA < (quadradoB + quadradoC):
        print('TRIANGULO ACUTANGULO')
    if lista [0] == lista[1] and lista[0] == lista[2]:
        print('TRIANGULO EQUILATERO')
    if lista [0] == lista[1] and lista[0] != lista[2]:
        print('TRIANGULO ISOSCELES')
    if lista [0] == lista[2] and lista[0] != lista[1]:
        print('TRIANGULO ISOSCELES')
    if lista [1] == lista[2] and lista[0] != lista[1]:
        print('TRIANGULO ISOSCELES')