n = int(input())
m = int(input())
bus = [[1e9]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a-1][b-1] = min(bus[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if bus[i][k] and bus[k][j]:
                bus[i][j] = min(bus[i][j], bus[i][k]+bus[k][j])

for i in range(n):
    for j in range(n):
        print(0 if bus[i][j] == 1e9 else bus[i][j], end=' ')
    print()
