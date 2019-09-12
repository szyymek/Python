def potega(a,n):
    if n==0:
        return 1
    else:
        return a*potega(a,n-1)
    
print(potega(5,3))
