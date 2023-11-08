from collections import deque


n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    gram = 1e9
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if (r, c) == (n-1, m-1):
            return min(visited[r][c]-1, gram)
        if arr[r][c] == 2:
            gram = (visited[r][c]-1)+(n-1-r)+(m-1-c)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] == 0 or arr[nr][nc] == 2:
                    visited[nr][nc] = visited[r][c]+1
                    queue.append((nr, nc))
    return gram


res = bfs()
print(res if res <= t else 'Fail')
