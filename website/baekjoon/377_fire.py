from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(queue, now):
    next_queue = deque()
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if now == '*':
                if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '#' and arr[nr][nc] != '*':
                    arr[nr][nc] = '*'
                    next_queue.append((nr, nc))
            else:
                if not 0 <= nr < h or not 0 <= nc < w:
                    global flag
                    flag = True
                    return deque()
                else:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = '@'
                        next_queue.append((nr, nc))
    return next_queue


for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    fq, sq = deque(), deque()
    for r in range(h):
        for c in range(w):
            if arr[r][c] == '*':
                fq.append((r, c))
            elif arr[r][c] == '@':
                sq.append((r, c))

    flag, count = False, 0
    while sq:
        fq = move(fq, '*')
        sq = move(sq, '.')
        count += 1

    if flag:
        print(count)
    else:
        print('IMPOSSIBLE')
