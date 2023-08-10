from collections import deque


t = int(input())

dr = [2, 1, -1, -2, -2, -1, 1, 2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    l = int(input())
    data = [[0] * l for _ in range(l)]
    s_r, s_c = map(int, input().split())
    g_r, g_c = map(int, input().split())

    queue = deque([(s_r, s_c)])
    while queue:
        r, c = queue.popleft()
        if r == g_r and c == g_c:
            break
        for i in range(len(dr)):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < l and 0 <= nc < l and data[nr][nc] == 0:
                data[nr][nc] = data[r][c] + 1
                queue.append((nr, nc))

    print(data[g_r][g_c])
