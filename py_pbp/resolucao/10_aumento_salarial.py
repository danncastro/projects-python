#python3

'''
AUMENTO SALARIAL: Faça um programa que calcule o aumento de um salário. 
1 -  Ele deve solicitar o valor do salário e a porcentagem do aumento. 
2 -  Exiba o valor do aumento e do novo salário
'''

salario = float(input('Digite o valor de salario: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))

percentual_aumento = porcentagem / 100
valor_aumento = salario * percentual_aumento
aumento_final = salario + valor_aumento

print(f'Houve um aumento de {porcentagem:.0f}% no salario, aumentando R${valor_aumento:.2f}, o salario atual é de: R${aumento_final:.2f}')
