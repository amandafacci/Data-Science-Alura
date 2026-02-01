bacA = 4
bacB = 10
contador = 0
while bacA < bacB:
    bacA = bacA + (bacA * (3 / 100))
    bacB = bacB + (bacB * (1.5 / 100))
    contador += 1
print('Bacteria A esta no tamanho', bacA)
print('Bacteria B esta no tamanho', bacB)
print('Foram necessarios', contador, 'dias para a bacteria A ultrapassar a B')
