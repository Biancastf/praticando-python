at_a = int(input('informe os dias para a atividade A:'))
at_b = int(input('informe os dias para a atividade B:'))
at_c = int(input('informe os dias para a atividade C:'))

if (at_a >=0 and at_b >=0 and at_c >=0):
  tempo_total = at_a + at_b + at_c
  print(f'o tempo total do projeto é de {tempo_total} dias')
else:
    print('Erro: Os dias não podem ser negativos.')
    