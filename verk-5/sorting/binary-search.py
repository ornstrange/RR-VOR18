#!/usr/bin/python
import sys
from math import floor

# Pseudo code
"""
1. Let min = 0 and max = n-1.
2. Compute guess as the average of max and min, rounded down (so that it is an integer).
3. If array[guess] equals target, then stop. You found it! Return guess.
4. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
5. Otherwise, the guess was too high. Set max = guess - 1.
6. Go back to step 2.
"""

def binary_search(query, arr):
    bot = 0
    top = len(arr) - 1
    found = False

    while bot <= top and not found:
        guess = (bot + top) // 2
        if arr[guess] == query:
            found = True
        elif arr[guess] > query:
            top = guess - 1
        else:
            bot = guess + 1
    return "Yes! its at index: %d" % guess if found else "I didn't find shit..."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = int(sys.argv[1].strip())
    else:
        query = 10
    if len(sys.argv) > 2:
        arr = sys.argv[2].split(",")
        arr = list(map(lambda x: int(x), arr))
    else:
        arr = [1,2,4,5,6,7,8,9,10,70,125,220,260,990,1050]
    output = "is " + str(query) + " in: " + str(arr) + "? " + str(binary_search(query, arr)) + "\n"
    sys.stdout.write(output)
