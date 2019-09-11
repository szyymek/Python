def solution(string,markers):
    l=[]
    l=string.split("\n")
    c=[]
    for zdanie in l:
        sygnal=0
        for x in zdanie:
            if x in markers:
                c.append(zdanie[:zdanie.index(x)])
                sygnal=1
                break
        if sygnal==0:
            c.append(zdanie)
    f=[]
    for zdanie in c:
        f.append(zdanie.rstrip())
    wynik=""
    for zdanie in f:
        wynik+=zdanie+"\n"
    return wynik[:-1]
