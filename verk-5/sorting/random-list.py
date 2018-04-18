#!/usr/bin/python
import sys
import random

if __name__ == "__main__":
    size = 50
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    rand_list = random.sample(range(500), size)
    output = ",".join(str(x) for x in rand_list) + "\n"
    sys.stdout.write(output)

    try:
        sys.stdout.close()
    except:
        pass
    try:
        sys.stderr.close()
    except:
        pass
