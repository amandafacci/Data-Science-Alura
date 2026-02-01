num = int(input('Informe um numero inteiro: '))
fatorial = 1
i = num 
while i > 0:
    fatorial *= i
    i -= 1
print(f'Fatorial de {num} e {fatorial}')
