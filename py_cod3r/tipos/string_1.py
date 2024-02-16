# Tipo Strings

print(dir(str)) # Retorna as funcionalidades disponiveis na função string

nome = 'Danniel Castro' # Atribui um texto a variavel nome
print(nome) # Retorna o conteúdo atribuido a variavel
print(nome[0]) # Retorna em formato de indice o valor 0 da atribuição da variavel

# nome[0] = 'P' # Gerará um erro pois não é possivel alterar um valor de indice especifico atribuido a uma variavel

# print('Marca d 'água') # Gerará um erro de sintax pois está escapando o valor da string
print("Danniel D' Castro") # Resolveria o problema de sintaxe sitado acima
print('Danniel D\' Castro') # Outro metodo de resolução do problema de sintaxe

texto = 'Texto entre apostrófos pode ter "aspas"' # Apenas demonstrando que o contrario também pode funcionar
print(texto)

doc = """Texto com múltiplas
    ... linhas"""
print(doc)

doc2 = '''Também é possível
    ... com 3 aspas simples'''
print(doc2)

doc2 = '''Também é possível...\t utilizar tab'''
print(doc2)