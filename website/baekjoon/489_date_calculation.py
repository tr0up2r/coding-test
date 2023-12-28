E, S, M = map(int, input().split())
e, s, m, y = 0, 0, 0, 0
while not (E == e and S == s and M == m):
    e, s, m = e%15+1, s%28+1, m%19+1
    y += 1
print(y)
