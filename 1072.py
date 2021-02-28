#Intervalo 2
num = int(input())
contin = 0
contout = 0

for i in range(num):
    a = int(input())
    if (a >= 10 and a <= 20):
        contin = contin + 1
    else:
        contout = contout + 1

print(f'{contin} in')
print(f'{contout} out')