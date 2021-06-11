#Sequencia IJ 4
I = 0
J = 1

while I <= 2:
    for X in range(1,4):
        if int(I) == I:
            print("I={:.0f} J={:.0f}".format(I,J))
        else:
            print("I={:.1f} J={:.1f}".format(I,J))

        J += 1

    I = round(I + 0.2, 1)
    J = round(J - 2.8, 1)