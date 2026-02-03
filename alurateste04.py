temp = float(input('Qual a temperatura em C? '))
contador = 0
soma = 0
while temp != -273:
    soma += temp
    contador += 1
    temp = float(input('Qual a temperatura em C? '))
media = soma / contador
print(f'A media das temperaturas e de: {media}')