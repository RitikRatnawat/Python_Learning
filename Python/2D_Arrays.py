"""Learning about 2D pipArrays in Python"""

import numpy as np

data = [[11, 15, 10, 6],
        [10, 14, 11, 5],
        [13, 56, 2, 67],
        [10, 45, 9, 23]]


# Creating a 2D Array
print("Creating a 2D Array")
arr2D = np.array(data)
print(arr2D, "\n")

# Inserting into the 2D Array
# axis = 0 means add as a row
# axis = 1 means add as a column
print("Inserting into the 2D Array")
new_arr2D_1 = np.insert(arr2D, 2, [[33, 4, 17, 11]], axis=1)
new_arr2D_2 = np.insert(arr2D, 2, [[33, 4, 17, 11]], axis=0)
print("With axis = 1 \n", new_arr2D_1, "\n")
print("With axis = 0 \n", new_arr2D_2, "\n")

new_arr2D_3 = np.append(arr2D, new_arr2D_1, axis=1)
new_arr2D_4 = np.append(arr2D, [[10, 34, 22, 15]], axis=0)
print("With axis = 1 \n", new_arr2D_3, "\n")
print("With axis = 0 \n", new_arr2D_4, "\n")

# Accessing an Element from the 2D Array
def accessElements(arr, row, col):
    n = len(arr)
    m = len(arr[0])

    return "Index is Out of Bound" if row >= n or col >= m else arr[row][col]
        
print("Get Element at row 2 and column 3 :", accessElements(arr2D, 2, 3))
print("Get Element at row 1 and column 4 :", accessElements(arr2D, 1, 4))
