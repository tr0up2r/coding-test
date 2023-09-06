from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        r, c, b = queue.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][b]

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc][b]:
                if arr[nr][nc] == 0:
                    queue.append((nr, nc, b))
                    visited[nr][nc][b] = visited[r][c][b]+1
                    continue
                if arr[nr][nc] == 1 and not b:
                    queue.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][b]+1
    return -1


print(bfs())
