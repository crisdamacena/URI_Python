#Multiplos
A,B=list(map(int,input().split()))

def multiplo(A,B):
    if B%A==0:
        return 'Sao Multiplos'
    elif A%B==0:
        return 'Sao Multiplos'
    else:
        return 'Nao sao Multiplos'

print(multiplo(A,B))