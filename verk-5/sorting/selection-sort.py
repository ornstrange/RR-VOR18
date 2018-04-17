#!/usr/bin/python
import sys

# Pseudo code
"""
1. At each iteration find the smallest entry (the "key") in the unsorted portion of the array.
2. Swap the "key" with the the ith entry.

lst = list / array
func selsrtI(lst)
    max = length(lst) - 1

    for i from 0 to max
        key = lst[i]
        keyj = i

        for j from i+1 to max
            if lst[j] < key
                key = lst[j]
                keyj = j

        lst[keyj] = lst[i]
        lst[i] = key

    return lst

end func
"""

def selection_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        keyj = i
        for j in range(i+1, len(arr)):
            if arr[j] < key:
                key = arr[j]
                keyj = j
        arr[keyj] = arr[i]
        arr[i] = key
    return arr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arr = sys.argv[1].split(',')
        arr = list(map(lambda x: int(x), arr))
    else:
        arr = [5,3,7,1]
    output = str(arr) + " sorted: " + str(selection_sort(arr)) + "\n"
    sys.stdout.write(output)
