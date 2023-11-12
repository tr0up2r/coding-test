from collections import deque


K = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

hr = [-2, -1, 1, 2, 2, 1, -1, -2]
hc = [1, 2, 2, 1, -1, -2, -2, -1]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[[0]*(K+1) for _ in range(w)] for _ in range(h)]


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while queue:
        r, c, k = queue.popleft()
        if r == h-1 and c == w-1:
            return visited[r][c][k]-1

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < h and 0 <= nc < w and not arr[nr][nc] and not visited[nr][nc][k]:
                visited[nr][nc][k] = visited[r][c][k]+1
                queue.append((nr, nc, k))
        if k < K:
            for i in range(8):
                nr, nc = r+hr[i], c+hc[i]
                if 0 <= nr < h and 0 <= nc < w and not arr[nr][nc] and not visited[nr][nc][k+1]:
                    visited[nr][nc][k+1] = visited[r][c][k]+1
                    queue.append((nr, nc, k+1))

    return -1


print(bfs())
