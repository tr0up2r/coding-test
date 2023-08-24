from collections import deque


m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque([(r, c)])
    visited = [[False]*n for _ in range(m)]
    visited[r][c] = True
    cheese = set()

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                if arr[nr][nc] == 1:
                    cheese.add((nr, nc))
                else:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r, c in cheese:
        arr[r][c] = 0

    return sum(list(map(sum, arr)))


count, answer = 0, sum(list(map(sum, arr)))
while True:
    now = bfs(0, 0)
    count += 1
    if now == 0:
        break
    answer = now

print(count)
print(answer)
