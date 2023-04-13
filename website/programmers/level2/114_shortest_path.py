from collections import deque


def solution(maps):
    # 하 우 상 좌
    n, m = len(maps), len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    if (nx, ny) == (n - 1, m - 1):
                        return maps[nx][ny]
        return maps[n - 1][m - 1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
