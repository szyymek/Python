def string_transformer(s):
    s = s.split(" ")
    s = s[::-1]
    print(s)
    s = " ".join(s)
    print(s)
    result = ""

    for letter in s:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result += letter.lower()
        else:
            result +=letter
    
    return result


#to jest rozwiązanie
