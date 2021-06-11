#Soma de Ímpares Consecutivos II
num = int(input())

for i in range(num):
    A,B=list(map(int,input().split()))
    if A > B:
        inicio = B
        fim = A
    if B >= A:
        inicio = A
        fim = B

    soma = 0
    for x in range(inicio+1,fim):
        if x %2 != 0:
            soma = soma + x
    print(soma)
