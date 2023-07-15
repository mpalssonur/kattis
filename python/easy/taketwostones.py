import sys

for i in sys.stdin:
    l = i.split()

    N = int(l[0])

    if N % 2 == 0:
        print("Bob")
    else:
        print("Alice")