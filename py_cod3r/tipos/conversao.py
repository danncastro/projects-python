# Conversão de Tipos

a = 2 # Variavel a recebe o valor 2
b = '3' # Variavel b recebe o valor 3
print(type(a)) # Retorna o tipo da variavel a, que no caso é um inteiro
print(type(b)) # Retorna o tipo da variavel b, que no caso é uma string

print(a + int(b)) # Converte a variavel b que é uma string em um número inteiro
print(str(a) + b) # Converte a variavel a que é um número inteiro em uma string

print(type(str(a))) # Retorna que a variavel a é uma string, mesmo que inicialmente ela tenha sido atribuida como inteiro

print(2 + int('2 Bom número')) # Ocorrerá um erro, pois mesmo que estejamos convertendo a expressão em um inteiro, não é possivel converter texto em base 10 