import numpy as np
import time
import random

a = [random.randrange(0,1000000) for i in range(1000000)]

start = time.time()
np.sort(a, kind='mergesort')
end = time.time()
print(end - start)

start = time.time()
np.sort(a, kind='heapsort')
end = time.time()
print(end - start)

start = time.time()
np.sort(a, kind='quicksort')
end = time.time()
print(end - start)
