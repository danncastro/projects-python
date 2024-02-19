#!python3

'''
A Empresa X determinou o aumento de 15% dos salários dos funcionários.
1 - O salário atual é de R$ 750,00.
2 - Execute um programa de acordo com o enunciado.
'''
salario = 750
aumento = 15
novo_salario = salario + (salario * aumento / 100)

print(f'Houve um aumento de 15% no salario, valor atualizado: R${novo_salario:.2f}')
