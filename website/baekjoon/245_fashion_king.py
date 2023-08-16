from functools import reduce


t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
        continue
    d = dict()

    for _ in range(n):
        category = input().split()[1]
        if category not in d.keys():
            d[category] = 1
        else:
            d[category] += 1

    counts = list(map(lambda x: x+1, d.values()))
    print(reduce(lambda x, y: x * y, counts)-1)
