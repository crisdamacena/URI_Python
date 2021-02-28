#Experiências
num = int(input())
quantidadetotal = 0
qcoelhos = 0
qratos = 0
qsapos = 0

for i in range(num):
    entrada = input().split()
    valor1, valor2 = entrada
    A = int(valor1)
    B = str(valor2)
    quantidadetotal = quantidadetotal + A
    if B == 'C':
        qcoelhos = qcoelhos + A
    if B == 'R':
        qratos = qratos + A
    if B == 'S':
        qsapos = qsapos + A
        
print(f'Total: {quantidadetotal} cobaias')
print(f'Total de coelhos: {qcoelhos}')
print(f'Total de ratos: {qratos}')
print(f'Total de sapos: {qsapos}')
print('Percentual de coelhos: {0:.2f} %'.format(((qcoelhos*100.0)/quantidadetotal)))
print('Percentual de ratos: {0:.2f} %'.format(((qratos*100.0)/quantidadetotal)))
print('Percentual de sapos: {0:.2f} %'.format(((qsapos*100.0)/quantidadetotal)))