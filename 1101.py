#Sequência de Números e Soma

while True:
    M,N=list(map(int,input().split()))
    if (M>0 and N>0):
        if M > N:
            inicio = N
            fim = M
        if N >= M:
            inicio = M
            fim = N

        soma = 0
        for x in range(inicio,fim+1):
            print(x, end=' ')
            soma = soma + x
        print(f'Sum={soma}')
    else:
        break