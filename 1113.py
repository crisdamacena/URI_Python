#Crescente e Decrescente

while True:
    X,Y=list(map(int,input().split()))
    if (X != Y):
        if Y > X:
            print('Crescente')
        if X > Y:
            print('Decrescente')
    else:
        break