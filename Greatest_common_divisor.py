def mygcd(x,y):
    if x%y == 0:
        return y
    else:
        return mygcd(y,x%y)
    
print(mygcd(18,3))
