# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# • Mostre a quantidade de valores que foram lidos;
# • Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# • Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# • Calcule e mostre a soma dos valores;
# • Calcule e mostre a média dos valores;
# • Calcule e mostre a quantidade de valores acima da média calculada;
# • Calcule e mostre a quantidade de valores abaixo de sete;
# • Encerre o programa com uma mensagem;

valores = []
soma = media = acima_media = abaixo_sete = 0
print('Digite alguns números. Para sair do programa, digite "-1".\n')
while True:
    n = float(input('Número: '))
    if n == -1:
        print()
        break
    elif n < -1:
        print('Número inválido.')
    else:
        valores.append(n)
print(f'Você digitou {len(valores)} números.')
print('Os números digitados foram: ', end='')
print(*valores, sep=', ', end='.\n')
print('A ordem inversa destes números, um abaixo do outro, são:')
for index in range(0, len(valores)):
    print(list(reversed(valores))[index])
    soma += valores[index]
media = soma / len(valores)
print(f'A soma dos valores digitados é igual a {soma:.1f}.')
print(f'A média dos valores digitados é igual a {media:.1f}.')
for index in range(0, len(valores)):
    if valores[index] > media:
        acima_media += 1
    elif valores[index] < 7:
        abaixo_sete += 1
if acima_media == 0:
    print('Você não digitou nenhum número acima da média calculada.')
elif acima_media == 1:
    print('Você digitou 1 número acima da média calculada.')
elif acima_media > 1:
    print(f'Você digitou {acima_media} números acima da média calculada.')
if abaixo_sete == 0:
    print('Você não digitou nenhum número abaixo de 7.')
elif abaixo_sete == 1:
    print('Você digitou 1 número abaixo de 7.')
elif abaixo_sete > 1:
    print(f'Você digitou {abaixo_sete} números menor que 7.')
print()
print('Fim do programa.')
