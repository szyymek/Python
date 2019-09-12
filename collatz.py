import matplotlib.pyplot as plt

def collatz(n):
    x=[]
    y=[]
    wynik=0
    while n!=1:
        if n%2==0:
            n=n/2
            wynik+=1
            y.append(n)
            x.append(wynik)
        else:
            n=(n*3)+1
            wynik+=1
            y.append(n)
            x.append(wynik)
    plt.plot(x,y)
    return wynik

print(collatz(27))
