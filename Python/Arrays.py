"""Learning about Arrays in Python"""

from array import *

# Creating an Integer Array
arr1 = array('i', [1, 2, 3, 4, 5, 6])
print("Integer Array :", arr1)

# Creating an Double Array
arr2 = array('d', [1.3, 2.9, 3.6])
print("Double Array :", arr2)

# Inserting an Element
arr1.insert(6, 7)
print("Array after Inserting Element :", arr1)

# Traversing over Array
print("Array Traversal :", end=" ")
for i in arr1:
    print(i, end=" ")
print()
    
# Accessing an Element
def accessElement(arr, index):
    return "No Element at these index" if index >= len(arr) else arr[index]
        
print("Element at index 4 :", accessElement(arr1, 4))
print("Element at index 10 :", accessElement(arr1, 10))

# Searching an Element
def searchElement(arr, element):
    return next((arr.index(element) for i in arr if i == element),
                "The element doesn't exist in the Array")

print("Element 5 in Array is at index :", searchElement(arr1, 5))
print("Element 0 in Array is at index :", searchElement(arr1, 0))

# Deleting an Element
def deleteElement(arr, element):
    for i in arr:
        if i == element:
            arr.remove(element)
            
    return "The element doesn't exist in the Array"
    
deleteElement(arr1, 5)
print("Array after Deleting 5 :", arr1)
deleteElement(arr1, 8)
print("Array after Deleting 8 :", arr1)