#Dividindo X por Y

n = int(input())

for i in range(n):
    X,Y=list(map(int,input().split()))
    if Y != 0:
        print(float(X/Y))
    else:
        print('divisao impossivel')