#Aumento de salário
renda = eval(format(float(input()), '.2f'))
taxa = float(0.0)
faixa1 = 0.08
faixa2 = 0.18
faixa3 = 0.28


if renda >= 0 and renda <= 2000.00:
    print('Isento')
    exit()
if renda >= 2000.01 and renda <= 3000.00:
    base = renda-2000.00
    taxa = faixa1 * base
    print('R$ {0:.2f}'.format(taxa))
    exit()
if renda >= 3000.01 and renda <= 4500.00:
    base = renda-3000.00
    taxa = (1000.00 * faixa1) + (base * faixa2)
    print('R$ {0:.2f}'.format(taxa))
    exit()
if renda > 4500.00:
    base = renda-4500.00
    taxa = (1000.00 * faixa1) + (1500.00 * faixa2) + (base * faixa3)
    print('R$ {0:.2f}'.format(taxa))
    exit()