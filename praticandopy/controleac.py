hora_atual = int(input('digite a hora atual (formato 24 horas): '))
if 8 <= hora_atual < 18:
    print('acesso permitido')
else:
    print('acesso negado')