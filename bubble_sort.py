def bombel(a):
    flaga=True
    for j in range(0,len(a)):
        if flaga==False:
            return a
        flaga=False
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                flaga=True
    return a

print(bombel([1,3,10,15,13,23,21,98]))
