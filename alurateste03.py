for nota_aluno in range(1,16):
    nota = float(input('Digite a nota: '))
    while nota < 0 or nota > 5:
        print('Nota invalida')
        nota = float(input('Digite a nota: '))
    print('Nota: ', nota)
print('Todas as notas foram inseridas')
