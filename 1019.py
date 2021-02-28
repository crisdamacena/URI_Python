#Conversão de tempo
tempo = int(input())
hora = int(tempo/3600)
tempo = tempo%3600
minuto = int(tempo/60)
tempo = tempo%60
segundo = tempo

print('{}:{}:{}'.format(hora, minuto, segundo))
