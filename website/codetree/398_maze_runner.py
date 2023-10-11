from collections import deque


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
runners = []
counts = [[0]*n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = '*'
    counts[r-1][c-1] += 1

out = list(map(int, input().split()))
out[0] -= 1
out[1] -= 1
arr[out[0]][out[1]] = 'E'


def get_smallest_square(arr, min_square):
    for r in range(n-min_square+1):
        for c in range(n-min_square+1):
            e_flag, p_flag = False, False
            for a in arr[r:r+min_square]:
                if 'E' in a[c:c+min_square]:
                    e_flag = True
                if '*' in a[c:c+min_square]:
                    p_flag = True
                if e_flag and p_flag:
                    return r, c


def rotate_square(arr, sr, sc, size, target):
    before = [[0]*size for _ in range(size)]
    after = [[0]*size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            before[r][c] = arr[sr+r][sc+c]

    for r in range(size):
        for c in range(size):
            if target == 'arr':
                if before[r][c] != '*' and before[r][c] != 'E' and before[r][c] > 0:
                    before[r][c] -= 1
            after[c][size-r-1] = before[r][c]

    for r in range(size):
        for c in range(size):
            arr[sr+r][sc+c] = after[r][c]

    return arr


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans_dist = 0

runners = deque()
for r in range(n):
    for c in range(n):
        if arr[r][c] == '*':
            runners.append((r, c))
        elif arr[r][c] == 'E':
            out = [r, c]
while k:
    to_move = []
    while runners:
        outflag = False
        r, c = runners.popleft()
        pos = []
        distance = abs(r-out[0])+abs(c-out[1])
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 'E':
                    arr[r][c] = 0
                    ans_dist += counts[r][c]
                    counts[r][c] = 0
                    outflag = True
                    break
                if (not arr[nr][nc] or arr[nr][nc] == '*') and abs(nr-out[0])+abs(nc-out[1]) <= distance:
                    pos.append((nr, nc))
        if not outflag and pos:
            arr[r][c], arr[pos[0][0]][pos[0][1]] = 0, '*'
            ans_dist += counts[r][c]
            if counts[pos[0][0]][pos[0][1]] and pos[0] in runners:
                to_move.append([r, c, pos[0][0], pos[0][1], counts[r][c]])
            else:
                counts[pos[0][0]][pos[0][1]] += counts[r][c]
                counts[r][c] = 0

    while to_move:
        sr, sc, gr, gc, v = to_move.pop()
        counts[gr][gc] += v
        counts[sr][sc] = 0
        arr[sr][sc], arr[gr][gc] = 0, '*'

    if not sum(map(sum, counts)):
        break

    min_square = n
    queue = deque([out])
    visited = [[0]*n for _ in range(n)]
    visited[out[0]][out[1]] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if arr[nr][nc] == '*':
                    min_square = min(max(abs(nr-out[0]), abs(nc-out[1])), min_square)
                visited[nr][nc] = 1
                queue.append((nr, nc))
    r, c = get_smallest_square(arr, min_square+1)
    arr = rotate_square(arr, r, c, min_square+1, 'arr')
    counts = rotate_square(counts, r, c, min_square+1, 'counts')

    runners = deque()
    for r in range(n):
        for c in range(n):
            if arr[r][c] == '*':
                runners.append((r, c))
            elif arr[r][c] == 'E':
                out = [r, c]

    k -= 1

print(ans_dist)
print(out[0]+1, out[1]+1)
