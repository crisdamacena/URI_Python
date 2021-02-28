#O maior
entrada = input().split()
valor1, valor2, valor3 = entrada
A = int(valor1)
B = int(valor2)
C = int(valor3)

maiorAB = ((A+B+abs(A-B))/2)
maiorABC = ((maiorAB+C+abs(maiorAB-C))/2)

print('{} eh o maior'.format(int(maiorABC)))