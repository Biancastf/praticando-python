distancia = float(input('digite a distância percorrida (em km): '))
if distancia < 100:
    print('valor do pedágio R$10')
elif 100 < distancia <= 200:
    print('valor do pedágio R$20')
else:
    print('valor do pedágio R$30')
    
    