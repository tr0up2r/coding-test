n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    print(data[i][0], data[i][1])
