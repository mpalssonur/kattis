n = int(input().strip())

total = 0.0
for i in range(n):
    line = input()

    q, y = [eval(i) for i in line.split()]
    total += q*y

print(total)
