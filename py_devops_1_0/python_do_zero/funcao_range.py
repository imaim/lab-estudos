numeros = range(100)
print(type(numeros))
print(list(numeros))

print('')
numeros_impar = []
numeros_par = []
for numero in numeros:
    print(f'O valor do range é: {numero}')
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(f'Numeros par: {numeros_par}')
print(f'Numeros impar: {numeros_impar}')