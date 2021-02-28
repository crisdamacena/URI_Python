#DDD
lista_telefonica = [('61','Brasilia'),('71','Salvador'),('11','Sao Paulo'),('21','Rio de Janeiro'),('32','Juiz de Fora'),('19','Campinas'),('27','Vitoria'),('31','Belo Horizonte')]
contatos = dict(lista_telefonica)

DDD = input()

if DDD in contatos:
    print(contatos[DDD])
else:
    print('DDD nao cadastrado')
