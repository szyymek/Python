def scalanie(a,b):
    wynik=[]
    while a!=[] or b!=[]:
        if a == []:
            for elementb in b:
                wynik.append(elementb)
                b.remove(elementb)
        elif b == []:
            for elementa in a:
                wynik.append(elementa)
                a.remove(elementa)
        elif a[0] <= b[0]:
            wynik.append(a[0])
            a.remove(a[0])
        else:
            wynik.append(b[0])
            b.remove(b[0])
    return wynik

def mergesort(T):
    if len(T)<=1:
        return T
    lewy=T[:int(len(T)/2)]
    prawy=T[int(len(T)/2):]
    lewy=mergesort(lewy)
    prawy=mergesort(prawy)
    return scalanie(lewy,prawy)

print(mergesort([8,3,10,15,2,13,5,2,98]))
