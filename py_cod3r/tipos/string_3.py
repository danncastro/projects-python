# Tipo String

frase = 'Python é uma linguagem excelente' # Atribui uma string a variavel
print('py' in frase) # Retorna um valor booleano(False) caso a palavra 'py' em minusculo esteja presente na variavel
print('ing' in frase) # Retorna um valor booleano(True) caso a palavra 'ing' em minusculo esteja presente na variavel
print('py' not in frase) # Retorna um valor booleano(True) caso a palavra 'py' em minusculo não esteja presente na variavel 

print(len(frase)) # Retorna a quantidade de caracteres atribuidos na variavel

print(frase.lower()) # Retorna todos os caracteres em letras minusculas
print('py' in frase.lower()) # Retorna um valor booleano(True) pois estamos transformando todos os caracteres em letras minusculas

print(frase.upper()) # Retorna todos os caracteres em letras maiusculas
print(frase) # Retorna o valor original da variavel

frase = frase.upper() # Altera definitivo o valor atribuido a variavel inicialmente
print(frase) # Retorna o novo valor atribuido a variavel

print(frase.split()) # Retorna a frase separada pelo espaços em branco
print(frase.split('A')) # Retorna a frase separada sem o caracter A