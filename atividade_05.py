# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# • A mensagem "Reprovado", se a média for menor do que sete;
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('Para calcular a média de um aluno, digite as duas notas parciais.\n')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print()
if media == 10:
    print(f'A média do aluno é {media:.1f}. O aluno foi aprovado com distinção.')
elif media >= 7:
    print(f'A média do aluno é {media:.1f}. O aluno foi aprovado.')
elif media < 7:
    print(f'A média do aluno é {media:.1f}. O aluno foi reprovado.')
