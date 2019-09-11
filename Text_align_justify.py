def justify(text, width):
    l=[]
    wynik=""
    koniec=width
    y=text.count(" ")
    while 1==1:
        ost_sp=text.rfind(" ",0,koniec+1)
        if ost_sp!=-1:
            l.append(text[0:ost_sp])
            text=text[ost_sp+1:]
            y-=1
            if len(text)<=width:
                l.append(text)
                break
            elif y==0:
                l.append(text)
                break
        else:
            sp=text.find(" ")
            l.append(text[0:sp])
            text=text[sp+1:]
            y-=1
            if y==0:
                l.append(text)
                break
    
    for i in l[0:len(l)-1]:
        tekst=""
        if i.count(" ") != 0:
            ilosc_krotkich_przerw=i.count(" ")-(width-len(i)+i.count(" "))%(i.count(" "))
            ilosc_dlugich_przerw=i.count(" ")-ilosc_krotkich_przerw
            dlugosc_krotkiej_przerwy=int((width-len(i)+i.count(" "))/(i.count(" ")))
            s=i.split()
            for k in range(0,ilosc_dlugich_przerw):
                tekst=tekst+s[k]+(" "*(dlugosc_krotkiej_przerwy+1))
            for j in range(ilosc_dlugich_przerw,ilosc_dlugich_przerw+ilosc_krotkich_przerw):
                tekst=tekst+s[j]+(" "*(dlugosc_krotkiej_przerwy))
            tekst=tekst+s[-1]
            wynik=wynik+tekst+"\n"
        else:
            wynik=wynik+i+"\n"
    wynik=wynik+l[-1]
    return wynik
