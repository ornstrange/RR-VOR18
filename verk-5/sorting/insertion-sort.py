#!/usr/bin/python
import sys

# Pseudo code
"""
1. Iterate through the array, starting from the second element:
    2. Note the element at this index.
    3. Walk back through the previous elements until you find a smaller element (or the beginning of the array), moving each element up by one.
    4. Insert the noted element at this point.

a = array og N = lengd
for i from 1 to N
   key = a[i]
   j = i - 1
   while j >= 0 and a[j] > key
      a[j+1] = a[j]
      j = j - 1
   a[j+1] = key
"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arr = sys.argv[1].split(",")
        arr = list(map(lambda x: int(x), arr))
    else:
        arr = [5,3,7,1]
    output = str(arr) + " sorted: " + str(insertion_sort(arr)) + "\n"
    sys.stdout.write(output)
