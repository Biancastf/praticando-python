peso = int(input('digite seu peso (kg): '))
altura = float(input('digite sua altura (m): '))
imc = peso / (altura ** 2)
print(f'seu IMC é: {imc:.2f}')
if imc < 18.5:
    print(f'abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'peso normal')
else:
    print(f'acima do peso')
    