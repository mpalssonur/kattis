import sys

for i in sys.stdin:
    n = int(i.strip())

    for i in range(n):
        print(str(i+1) + " Abracadabra")
