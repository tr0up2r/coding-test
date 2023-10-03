from collections import deque


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

wq, sq = deque(), deque()
for r in range(R):
    for c in range(C):
        if arr[r][c] == '*':
            wq.append((r, c))
        elif arr[r][c] == 'S':
            sq.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(queue, now, visited):
    next_queue = deque()
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if now == '*':
                    if arr[nr][nc] != 'D' and arr[nr][nc] != 'X':
                        arr[nr][nc] = '*'
                        next_queue.append((nr, nc))
                        visited[nr][nc] = True
                else:
                    if arr[nr][nc] == 'D':
                        global flag
                        flag = True
                        return next_queue, visited
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = 'S'
                        next_queue.append((nr, nc))
                        visited[nr][nc] = True
    return next_queue, visited


flag, answer = False, 0
w_visited, s_visited = [[False]*C for _ in range(R)], [[False]*C for _ in range(R)]
while sq:
    answer += 1
    wq, w_visited = move(wq, '*', w_visited)
    sq, s_visited = move(sq, 'S', s_visited)
    if flag:
        break

print(answer if flag else 'KAKTUS')
