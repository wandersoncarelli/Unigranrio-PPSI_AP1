# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Para calcular a média bimestral, digite a nota dos 4 bimestres.\n')

n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))
n3 = float(input('Nota do terceiro bimestre: '))
n4 = float(input('Nota do quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4

print()
print(f'A média bimestral é {media:.1f}.')
