import sys


n, m = map(int, input().split())
d = dict()
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if len(w) >= m:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
print('\n'.join(sorted(d, key=lambda x: (-d[x], -len(x), x))))
