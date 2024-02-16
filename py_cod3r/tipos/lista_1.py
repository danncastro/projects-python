# Tipo lista: Adição e remoção de elementos da lista

nums = [1, 2, 3]
print(f'Retorna os items adicionados a lista inicialmente - [{nums}]')

print(f'Retorna o tipo de função atribuida a variavel - [{type(nums)}]')
print(f'Retorna a quantidade de elementos atribuidos a função list - [{len(nums)}]') 

nums.append(3) # Adiciona um novo item ao final da lista
nums.append(4) # Adiciona outro item ao final da lista
nums.append(500) # Adiciona adiciona novamente outro item ao final da lista
print(f'Retorna a nova quantidade de elementos após a adição de novos items a função list - [{len(nums)}]')
print(f'Retorna os items adicionados a lista - [{nums}]')

nums[3] = 100 # Reatribui um valor ao elemento de indice 3
print(f'Retorna os elementos da lista com a alteração feita - [{nums}]')

nums.insert(0, -200) # Atribui ao indice 0 o item -200
print(f'Retorna os elementos da lista com o item adicionado ao indice zero - [{nums}]')

print(f'Retorna o elemento que está atribuido ao indice 6 - [{nums[6]}]')
print(f'Retorna o elemento que está atribuido ao indice -1, equivalente ao indice 6 - [{nums[-1]}]')
print(f'Retorna o elemento que está atribuido ao indice -2, começando de trás para frente - [{nums[-2]}]')

lista = []
# help(lista) # Retorna uma tela com ajuda da função
print(f'Retorna o tipo de função atribuido a variavel - [{type(lista)}]')
print(f'Retorna os metodos disponibilizados para a função list - [{dir(lista)}]')
print(f'Retorna a quantidade de elementos atribuidos a função list - [{len(lista)}]')

lista.append(1) # Atribui items a lista
lista.append(2) # Atribui novos items a lista
lista.append(3) # Atribui novos items a lista novamente
print(f'Retorna os novos elementos adicionados a função list - [{lista}]')

nova_lista = [1, 5, 'Danniel', 'Isabella'] # Atribui valore eterogenios a list
print(f'Retorna os items adicionados a lista inicialmente - [{nova_lista}]')

nova_lista.remove(5) # Remove o item 5 de dentro da list, não o indice 5
print(f'Retorna a lista de elementos com o item 5 removido - [{nova_lista}]')

nova_lista.reverse() # Retorna o novo valor alterado na variavel, de trás para frente
print(f'Retorna a lista de elementos de trás para frente - [{nova_lista}]')

lista.append([1, 2, 3]) # Atribui uma lista dentro da lista já existente
print(f'Retorna a atribuição de uma lista, dentro da função list já existente - [{lista}]')