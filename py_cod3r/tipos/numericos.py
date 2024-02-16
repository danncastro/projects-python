# Tipos Númericos

print(dir(int)) # Retorna as funcionalidas disponiveis na função Inteiros
print(dir(float)) # Retorna as funcionalidas disponiveis na função Float

a = 5 # Atribui o valor 5 a variavel a
b = 2.5 # Atribui o valor 2.5 a variavel b

print(type(a / b)) # Retorna um tipo Float, por que todas operações efetuadas com um float, retorna float
print(type(a + b)) # Retorna um tipo Float
print(type(a * b)) # Retorna um tipo Float

print(type(a)) # Retorna o tipo de função atribuido a variavel a
print(type(b)) # Retorna o tipo de função atribuido a variavel b

print(b.is_integer()) # Retorna um valor booleano de False para caso a variavel B não seja um inteiro 
print(5.0.is_integer()) # Retorna um valor booleano de True, por que embora o 5.0 seja um tipo Float, a 0 não é descartado na resolução

print(int.__add__(2, 3)) # Retorna a soma dos valores 2 + 3, a função __add__ está disponivel dentro do metodo Inteiro.

print((-2).__abs__()) # Retorna um valor sempre absoluto, seja ele Inteiro negativo
print(abs(-2)) # Metodo abreviado do metodo __abs__ utilzado pela função abs

print((-3.6).__abs__())  # Retorna um valor sempre absoluto, seja ele Float negativo
print(abs(3.6)) # Metodo abreviado do metodo __abs__ utilzado pela função abs

# Decimal

from decimal import Decimal, getcontext # Importa do modulo decimal, a função Decimal e getcontext unicamente.

print(Decimal(1) / Decimal(7)) # Retorna de forma decimal a divisão do de 1 por 7

getcontext().prec = 3 # Informa quantas casas decimais serão apresentadas em tela
print(Decimal(1.1) + Decimal(2.2)) # Retorna a soma dos valores 1.1 + 2.2 com a quantidade de casas decimais definidas em getcontext

import decimal # Importa todo o modulo decimal
print(dir(decimal)) # Retorna as funções disponibilizadas no modulo decimal