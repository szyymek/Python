#List is a collection which is ordered and changeable. Allows duplicate members.
lista_imion = ['Jan', 'Piotr', 'Marcin', 'Tomasz', 'Grzegorz']

#print range of list
print(lista_imion[2:4])

#change element of list
lista_imion[1] = 'Janusz'
print(lista_imion)

#Loop through the list
for i in lista_imion:
    print(i)
    
#add element to list
lista_imion.append('Marian')
print(lista_imion)

#add element to list on specific place
lista_imion.insert(2,'Wojciech')
print(lista_imion)

#sort list
lista_imion.sort()
print(lista_imion)

#remove specific list element
lista_imion.pop(3)
print(lista_imion)

#clear all elements of list
lista_imion.clear()
print(lista_imion)
