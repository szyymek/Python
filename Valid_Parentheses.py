def valid_parentheses(string):
    kontrola=0
    for znak in string:
        if kontrola<0:
            return False
        elif znak=="(":
            kontrola+=1
        elif znak==")":
            kontrola-=1
        else:
            continue
    if kontrola==0:
        return True
    else:
        return False
