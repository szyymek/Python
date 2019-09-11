def commas(num):
    napis=str(num)
    znak=""
    if num<0:
        znak="-"
    podzial=napis.split(".")
    odwrotnie=str(abs(int(podzial[0])))[::-1]
    wynik=""
    if len(podzial)==1 or round(float("0."+podzial[1]),3)==float(0):
        for x in range(0,len(odwrotnie)):
            if x%3==0:
                wynik+=','+odwrotnie[x]
            else:
                wynik+=odwrotnie[x]
        return znak+wynik[1:][::-1]
    else:
        for x in range(0,len(odwrotnie)):
            if x%3==0:
                wynik+=','+odwrotnie[x]
            else:
                wynik+=odwrotnie[x]
        if round(float("0."+podzial[1]),3)==float(1):
            cyferka=int(wynik[1:][::-1])+1
            inna=znak+str(cyferka)
            return commas(int(inna))
        else:
            liczba = round(float("0."+podzial[1]),3)
            return znak+wynik[1:][::-1]+str(liczba)[1:]
