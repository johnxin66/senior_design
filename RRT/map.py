import numpy as np
import binvox_rw

with open('sample.binvox', 'rb') as f:
    ms = binvox_rw.read_as_coord_array(f)

x = ms.data[0]
y = ms.data[1]
z = ms.data[2]

rows, cols = (1000,1000)
arr = [[0 for i in range(cols)] for j in range(rows)]

for i in range(len(x)):
    if (z[i] > 100): 
        xPos = x[i]
        yPos = y[i]
        arr[yPos][xPos] = 1
    else:
        for m in range(-5000, 5001, 1000):
            for n in range(-5, 6):
                if(i+n+m > 0 and i+n+m < 1000000):
                    if (z[i+n+m] > 100):
                        xPos = x[i]
                        yPos = y[i]
                        arr[yPos][xPos] = 1

with open('map.npy', 'wb') as f:
    np.save(f, arr)
