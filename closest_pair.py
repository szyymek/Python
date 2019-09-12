def dist(a,b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**(1/2)


def closest_pair(a):
    mindist=1000
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            p=a[i]
            q=a[j]
            if dist(p,q)<mindist:
                mindist=dist(p,q)
                closestpair=[p,q]                 
    return closestpair

print(closest_pair([(1,2),(2,4),(1,3),(2,5)]))
