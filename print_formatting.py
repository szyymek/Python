#Formatting with the .format() method
print("This is first string {}, and second {}".format('inside1', 'inside2'))
print("This is first string {0}, and first again {0}".format('inside1', 'inside2'))

#Formatting floats with specific precision
wynik = 100/33
print("Result is: {w:1.2f}".format(w=wynik))
print("Result is: {w:1.5f}".format(w=wynik))
