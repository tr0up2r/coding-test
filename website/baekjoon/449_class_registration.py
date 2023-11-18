k, l = map(int, input().split())
d = dict()
for i in range(l):
    d[input()] = i
for s in sorted(d, key=lambda x: d[x])[:k]:
    print(s)
