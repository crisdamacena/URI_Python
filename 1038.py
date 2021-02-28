#Lanche
entrada = input().split()
valor1, valor2 = entrada
codigo = int(valor1)
quantidade = int(valor2)
total = float()

if codigo == 1:
    preco = 4.0
    total = float(quantidade*preco)
    print('Total: R$ {0:.2f}'.format(total))
    exit()
if codigo == 2:
    preco = 4.5
    total = float(quantidade*preco)
    print('Total: R$ {0:.2f}'.format(total))
    exit()
if codigo == 3:
    preco = 5.0
    total = float(quantidade*preco)
    print('Total: R$ {0:.2f}'.format(total))
    exit()
if codigo == 4:
    preco = 2.0
    total = float(quantidade*preco)
    print('Total: R$ {0:.2f}'.format(total))
    exit()
if codigo == 5:
    preco = 1.5
    total = float(quantidade*preco)
    print('Total: R$ {0:.2f}'.format(total))
    exit()