import sys

for i in sys.stdin:
    l = i.split()

    h = int(l[0])
    b = int(l[1])

    a = h * b /2

    print(a)