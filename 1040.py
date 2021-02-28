#Media 3
entrada1 = input().split()
valor1, valor2, valor3, valor4 = entrada1
N1 = float(valor1)
N2 = float(valor2)
N3 = float(valor3)
N4 = float(valor4)

media = float(((N1*2.0)+(N2*3.0)+(N3*4.0)+(N4*1.0))/10)
print('Media: {0:.1f}'.format(media))

if media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    entrada2 = float(input())
    exame = entrada2
    print('Nota do exame: {0:.1f}'.format(exame))
    novamedia = float((media + exame)/2.0)
    if novamedia >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {0:.1f}'.format(novamedia))
    elif novamedia <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {0:.1f}'.format(novamedia))
elif media >= 7.0:
    print('Aluno aprovado.')