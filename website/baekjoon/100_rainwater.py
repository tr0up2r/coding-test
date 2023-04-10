h, w = map(int, input().split())
blocks = list(map(int, input().split()))
data = [[0]*w for _ in range(h)]

j = 0
for b in blocks:
    for i in range(b):
        data[i][j] = 1
    j += 1

max_b = max(blocks)
dy = [-1, 1]

result = 0
visited = [[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        rain = 0
        if visited[i][j]:
            continue
        if data[i][j] == 0:
            meet = 0
            rain += 1
            flag = False
            visited[i][j] = True
            for k in range(2):
                nj = j
                while True:
                    nj += dy[k]
                    if nj < 0 or nj >= w or visited[i][nj]:
                        rain = 0
                        flag = True
                        break
                    if data[i][nj] == 0:
                        visited[i][nj] = True
                        rain += 1
                    if data[i][nj] == 1:
                        meet += 1
                        break
                if flag:
                    break
                if meet == 2:
                    result += rain

print(result)
