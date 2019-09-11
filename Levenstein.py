import numpy as np

def sprawdz_podobienstwo(wzor, szukany_wyraz):
    return levenshtein_ratio_and_distance(wzor, szukany_wyraz ,ratio_calc = True)

print(sprawdz_podobienstwo('Bahamas', 'Banana'))


#------------------------------------------------------------------
# Below implementation of Levenstein distance was found in internet
#------------------------------------------------------------------

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k   
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 
            else:
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,
                                 distance[row][col-1] + 1,
                                 distance[row-1][col-1] + cost)

    Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
    return Ratio
