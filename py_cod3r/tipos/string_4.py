# Tipo String: Metodos magicos

a = '123' # Atribui uma string a variavel
b = ' de Oliveira 4' # Atribui uma string a variavel

print(a + b) # Soma os valores atribuidos as variaveis
print(a.__add__(b)) # Demostra como o metodo de soma é utilizado pela função
print(str.__add__(a, b)) # Mostra uma outra forma de soma de valores

print(dir(str)) # Retorna os metodos de disponibilizados pela função string

print(len(a)) # Retorna a quantidade de caracteres atribuidos a variavel a
print(a.__len__) # Retorna a quantidade de caractees atribuis a variavel, utilziando um metodo interno da função

print('1' in a) # Retorna um valor booleano(True), caso a letra 1 encontra-se atribuido a variavel a
print(a.__contains__('1')) # Valida se a variavel contem a letra 1 utilizando um metodo interno