from collections import deque


m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

tomato = deque([])

for r in range(n):
    for c in range(m):
        if data[r][c] == 1:
            tomato.append((r, c))

while True:
    flag = False
    new_tomato = deque([])
    while tomato:
        r, c = tomato.popleft()
        if data[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < n and 0 <= nc < m and data[nr][nc] == 0:
                    data[nr][nc] = 1
                    new_tomato.append((nr, nc))
                    flag = True
    tomato = new_tomato

    if not flag:
        break
    answer += 1

for x in data:
    if 0 in x:
        answer = -1
        break

print(answer)
