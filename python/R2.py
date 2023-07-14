import sys


for i in sys.stdin:
    l = i.split()
    r1 = int(l[0])
    s = int(l[1])

    r2 = 2 * s - r1

    print(r2)

