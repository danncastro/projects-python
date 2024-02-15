# Coerção Automática

print(type(10 / 2)) # Retorna uma classe do tipo Float

print(type(10 // 3)) # Retorna uma classe do tipo Inteiro, pois as duas barras representam uma divisão inteira em python

print(type(10 // 3.3)) # Retorna uma classe do tipo Float, mesmo utilizando as duas barras, o valor da divisão é um número flutuante.

print(type(10 / 2.5)) # Retorna uma classe do tipo Float

print(type(2 + True)) # Retorna uma classe do tipo Inteiro

print(type(2.5 + False)) # Retorna uma classe do tipo Float