# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# • calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato (5%) : R$
#   - Salário Líquido : R$
# Obs: Salário Bruto - Descontos = Salário Líquido.

print('Para calcular seu salário no mês, digite quando você ganha por hora e quantas horas trabalha no mês.\n')

salario_hora = float(input('Quanto você ganha por hora? \nR$'))
horas_trabalhadas = int(input('Quantas horas você trabalha por mês?\n'))

salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - ir - inss - sindicato

print()
print(f'Seu salário bruto é R${salario_bruto:.2f}.')
print(f'Você pagou R${ir:.2f} de imposto de renda.')
print(f'Você pagou R${inss:.2f} ao INSS.')
print(f'Você pagou R${sindicato:.2f} ao sindicato.')
print(f'Seu salário líquido é de R${salario_liquido:.2f}')
