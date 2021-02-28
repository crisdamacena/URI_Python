subreino = input()
classe = input()
alimentacao = input()

if subreino == "vertebrado":
    if classe == "ave":
        if alimentacao == "carnivoro":
            print('aguia')
        elif alimentacao == "onivoro":
            print('pomba')   
    elif classe == "mamifero":
        if alimentacao == "onivoro":
            print('homem')
        elif alimentacao == "herbivoro":
            print('vaca')         
elif subreino == "invertebrado":
    if classe == "inseto":
        if alimentacao == "hematofago":
            print('pulga')
        elif alimentacao == "herbivoro":
            print('lagarta') 
    elif classe == "anelideo":   
        if alimentacao == "hematofago":
            print('sanguessuga')
        elif alimentacao == "onivoro":
            print('minhoca') 
