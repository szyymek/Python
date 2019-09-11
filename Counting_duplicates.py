def duplicate_count(text):
    licznik=0
    policzone=[]
    slowo=text.lower()
    for i in slowo:
        if i not in policzone:
            policzone.append(i)
            if slowo.count(i)>1:
                licznik+=1
    return licznik
