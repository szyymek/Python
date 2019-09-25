import numpy as np

A = np.array([[1,-2,3],[-1,1,5],[-2,-1,1]]) #create matrix

#print(A)

B = np.array([[ 5, 10,  0]]).T #create transposed matrix
#print(B)

C = np.transpose(A) #transpose matrix
#print(C)

D = np.arange(0,2*np.pi,2*np.pi/100) 
sinusy = [np.sin(i) for i in D] #count sinus for 100 numbers between 0 and 2pi
#print(D)
#print(sinusy)

E = np.arange(12).reshape(3,4)
#print(E)
#print(E[:,[1,0,2,3]]) #swap column 1 and 2 in matrix
#print(E[[1,0,2], :]) #swap rows 1 and 2 in matrix
#print(E[::-1]) # reverse rows in matrix

F = np.random.randint(5, 11, size=(5,3)) #print matrix(5,3) of random integers between 5 and 10
#print(F)

norma = np.linalg.norm(F) #calculate matrix norm
#print(norma)

wyznacznik = np.linalg.det(A) #calculate matrix determinant
#print(wyznacznik)

iloczyn_skalarny = np.dot(A,B) # calculate dot product of arrays
#print(iloczyn_skalarny)

rownanie_algebraiczne = np.linalg.solve(A,B) #solve linearequation
#print(rownanie_algebraiczne)
