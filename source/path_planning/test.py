import numpy as np
import binvox_rw
with open('test_map_1000_1000_300.binvox', 'rb') as f:
    ms = binvox_rw.read_as_coord_array(f);
x = ms.data[0];
y = ms.data[1];
z = ms.data[2];
rows, cols = (1000,1000);
arr = [[0 for i in range(cols)] for j in range(rows)];
for i in range(len(x)):
    if (z[i] > 100):
        xPos = x[i];
        yPos = y[i];
        arr[yPos][xPos] = 1;
print(arr)