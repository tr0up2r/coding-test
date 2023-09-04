import sys
from collections import deque


dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(r, c):
    queue = deque([(r, c)])
    arr[r][c] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc]:
                queue.append((nr, nc))
                arr[nr][nc] = 0


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    answer = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c]:
                bfs(r, c)
                answer += 1
    print(answer)
    arr.clear()
