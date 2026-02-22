renda_mensal = float(input('digite o valor da sua renda mensal: '))
parcela = float(input('digite o valor da parcela desejada: '))
if renda_mensal > 2000 and parcela <= 0.3* renda_mensal:
    print('empréstimo aprovado')
elif renda_mensal <= 2000:
    print('empréstimo negado: renda mensal insuficiente')
else:
    print('empréstimo negado: parcela acima de 30% da renda mensal')
    