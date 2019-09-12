import numpy as np
import time
import random

a = [random.randrange(0,1000000) for i in range(1000000)]

kinds = ['mergesort', 'heapsort', 'quicksort']

for k in kinds:
    start = time.time()
    np.sort(a, kind=k)
    end = time.time()
    print(end - start)
