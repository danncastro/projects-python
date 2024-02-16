# Tipo String

nome = 'Danniel Gutierres' # Atribui uma string de 17 caracteres a variavel
nome2 = 'Isabella Carvalho' # Atribui uma string de 15 caracteres a variavel

print(nome[0]) # Retorna o elemento de indice 0 ou seja a letra D atribuida a variavel
print(nome[6]) # Retorna o elemento de indice 6 ou seja a letra l atribuida a variavel
print(nome[-11]) # Nesse caso a contagem começará de trás para frente contadas apartir do -1..-2... até -11 que equivale ao elemento 6
print(nome[8:]) # Retorna um range de elementos começados a partir do indice 4 para frente ou seja a palavra Gutierres
print(nome[-9:]) # Retorna um range de elementos começados a partir do ultimo elemento dos indices, ou seja de trás para frente
print(nome[:8]) # Retorna um range começados pelo indice 0 até a quantidade de elementos informados
print(nome[6:9]) # Retorna um range começados no 6 elemento do indice até o 9, ou seja as letras l e G

numeros = '1234567890' # Atribui uma string de 10 elementos a variavel
print(numeros) # Retorna todos os elementos atribuidos a variavel
print(numeros[::]) # Também retornará todos os elementos atribuidos, pois não passamos nenhum range, ou indice especifico
print(numeros[::2]) # Retorna os elementos atribuidos na variavel pulando de 2 em 2 indices
print(numeros[1::2]) # Retorna os elementos atribuidos na variavel pulando de 2 em 2 indices começados apartir do indice 1 incluindo ele
print(numeros[::-1]) # Retorna os elementos de forma invertida
print(numeros[::-2]) # Retorna os elementos de forma invertida pulando de 2 em 2 indices

# Exemplo
print(nome[::-1])
print(nome2[::-1])