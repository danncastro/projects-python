# Builtins

exemplo1 = type(1) # Retorna qual o tipo de classe está sendo atribuida a variavel
print(exemplo1)

exemplo2 = __builtins__.type('Fala Galera!') # Demonstra como a função type é chamado através da utilização do modúlo builtins
print(exemplo2)

exemplo3 = __builtins__.print('Fala Galera!') # Demonstra como a funcionalidade do print é chamado através da utilização do modúlo builtins

# help(dir) # Trás uma tela de ajuda que explica a funcionalidade informada
# __builtins__.help(__builtins__.dir)

print(dir()) # Trás o que está atribuido ao escopo global
print(dir(__builtins__)) # Trás informação das funcionalidas ou atribuições do parametro

# Exemplo real
nome = 'Danniel Gutierres de Castro'
print(type(nome))
print(__builtins__.len(nome))
print(dir())