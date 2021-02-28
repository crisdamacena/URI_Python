#Cálculo simples
peca1 =input().split()
peca2 =input().split()

codigo1, numero1, unitario1 = peca1
codigo2, numero2, unitario2 = peca2

conta1 = int(numero1)*float(unitario1)
conta2 = int(numero2)*float(unitario2)

total = conta1+conta2

print('VALOR A PAGAR: R$ {0:.2f}'.format(total))