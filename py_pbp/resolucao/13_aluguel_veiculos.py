#!/bin/python3

'''
ALUGUEL DE VEÍCULOS: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário.
1 - Assim como a quantidade de dias pelos quais o carro foi alugado. 
2 - Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
'''

quilometragem = float(input('Quilometragem percorrida: '))
dias_alugado = int(input('Quantos dias foi alugado: '))

preco_dia = 60
preco_quilometragem = 0.15

custo_dia = dias_alugado * 60
custo_quilometragem = quilometragem * preco_quilometragem

custo_total = custo_dia + custo_quilometragem

print(f'O valor total pelo aluguel de {dias_alugado} dias e {quilometragem:0.0f}km rodados é de: R${custo_total:.2f}')
