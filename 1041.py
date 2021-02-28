#Coordenadas de um ponto
entrada = input().split()
valor1, valor2 = entrada
x = float(valor1)
y = float(valor2)

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
elif x == 0 and y == 0:
    print('Origem')