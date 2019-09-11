def luck_check(string):
    srodek=len(string)
    if srodek%2==1:
        string=string[:int(srodek/2)]+string[(int(srodek/2))+1:]
    lewa=prawa=0
    for x in string[:int(srodek/2)]:
        lewa+=int(x)
    for y in string[int(srodek/2):]:
        prawa+=int(y)
    return prawa==lewa
