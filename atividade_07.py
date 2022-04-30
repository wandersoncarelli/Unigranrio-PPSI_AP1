# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
# ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

while True:
    n1 = int(input('Digite um número entre 1 e 10 para ver sua tabuada: '))
    if 0 < n1 < 11:
        break
    else:
        print('Número inválido.')
        print()

print()
print(f'Tabuada de {n1}:')
for index in range(1, 11):
    print(f'{n1} x {index} = {n1 * index}')
