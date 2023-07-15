import sys

for i in sys.stdin:
    l = i.split()

    a = int(l[0])
    b = int(l[1])

    if a > b:
        print(1)
    else:
        print(0)