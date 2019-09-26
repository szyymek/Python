#Tuples are ordered, similar as lists, but are unchangeable (immutable)
krotka_imion = ('Jan', 'Piotr', 'Marcin', 'Tomasz', 'Grzegorz')

#can be created from different types
krotka_cyfr = (1,2,3)
krotka_mieszana = ('Jan', 1)

#are indexed and can be sliced like a lists
print(krotka_imion[3], krotka_imion[1:3])

#return index of given value
print(krotka_imion.index('Jan'))

#return quality of given values
print(krotka_imion.count('Jan'))
