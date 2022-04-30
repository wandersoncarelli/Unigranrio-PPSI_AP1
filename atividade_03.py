# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:
# • Para homens: (72.7*h) - 58
# • Para mulheres: (62.1*h) - 44.7

print('Digite a altura para calcular o peso ideal.\n')

h = float(input('Altura: '))
peso_homem = (72.7 * h) - 58
peso_mulher = (62.1 * h) - 44.7

print()
print(f'Homens com {h}m de altura, o peso ideal é de {peso_homem:.2f}kg.')
print(f'Mulheres com {h}m de altura, o peso ideal é de {peso_mulher:.2f}kg.')
