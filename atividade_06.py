# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
# desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
#   - salário antes do reajuste;
#   - percentual de aumento aplicado;
#   - valor do aumento;
#   - novo salário, após o aumento.

print('Para calcular o reajuste de salário do colaborador, digite o salário atual.\n')

salario_atual = int(input('Salário atual do colaborador: \nR$'))
percentual = reajuste = 0

if salario_atual < 280:
    percentual = 20
    reajuste = salario_atual * percentual / 100
elif 280 <= salario_atual < 700:
    percentual = 15
    reajuste = salario_atual * percentual / 100
elif 700 <= salario_atual < 1500:
    percentual = 10
    reajuste = salario_atual * percentual / 100
else:
    percentual = 5
    reajuste = salario_atual * percentual / 100
novo_salario = salario_atual + reajuste

print()
print(f'O salário do colaborador antes do reajuste é de R${salario_atual:.2f}.')
print(f'O percentual de aumento aplicado no salário será de {percentual}%.')
print(f'O valor do aumento de salário do colaborador será de R${reajuste:.2f}.')
print(f'O novo salário do colaborador após o aumento, será de R${novo_salario:.2f}.')
