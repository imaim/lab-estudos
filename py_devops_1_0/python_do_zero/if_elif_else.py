'''
Sistema de calculo de IMC

O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros)

- Menor que 18,5 = Magreza
- Entre 18,5 e 24,9 = Normal
- Entre 25,0 e 29,9 = Sobrepeso
- Entre 30,0 e 39,9 = Obesidade
- Maior que 40,00 = Obesidade Grave
'''

altura = float(input('Digite sua Altura (Ex. : 1.72): '))
peso = float(input('Digite seu peso (Ex. : 72): '))

imc = peso / (altura**2)
# ** operador de potencia
imc = round(imc, 2)

if imc > 0 and imc < 18.5:
    print(f'Seu IMC {imc}, está categorizado como Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC {imc}, está categorizado como Normal')
elif imc >=25.0 and imc <= 29.9:
    print(f'Seu IMC {imc}, está categorizado como Sobrepeso')
elif imc >=30.0 and imc <= 39.9:
    print(f'Seu IMC {imc}, está categorizado como Obesidade')
elif imc > 40:
    print(f'Seu IMC {imc}, está categorizado como Obesidade Grave')
else:
    print('Erro nos valores declarados')
