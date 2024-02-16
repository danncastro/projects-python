# Conversão de Tipos: Alterando o tipo da variavel

a = 2 
b = '3'

print(f'Retorna o tipo da variavel A={a} - [{type(a)}]')
print(f'Retorna o tipo da variavel B={b} - [{type(b)}]')

print(f'Converte a variavel B em um número inteiro - [{a + int(b)}] [{type(b)}]') 
print(f'Converte a variavel A em uma string - [{str(a) + b}] [{type(a)}]') 

print(f'Retorna que a variavel A é uma String, mesmo que inicialmente ela tenha sido atribuida como inteiro - [{type(str(a))}]')

# print(2 + int('2 Bom número')) # Ocorrerá um erro, pois mesmo que estejamos convertendo a expressão em um inteiro, não é possivel converter texto em base 10 