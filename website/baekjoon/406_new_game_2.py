from collections import deque


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pieces = [[deque() for _ in range(n)] for _ in range(n)]
rc_info, d_info = dict(), dict()
for i in range(k):
    r, c, d = map(int, input().split())
    pieces[r-1][c-1].append(i)
    rc_info[i] = (r-1, c-1)
    d_info[i] = d-1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def main():
    for turn in range(1, 1001):
        for i in range(k):
            r, c = rc_info[i]
            d = d_info[i]
            for j in range(len(pieces[r][c])):
                if pieces[r][c][j] == i:
                    idx = j
                    break

            nr, nc = r+dr[d], c+dc[d]
            if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == 2:
                if d%2:
                    d -= 1
                else:
                    d += 1
                nr, nc = r+dr[d], c+dc[d]
                d_info[i] = d

            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 2:
                next = deque()
                for _ in range(len(pieces[r][c])-idx):
                    now = pieces[r][c].pop()
                    if board[nr][nc] == 0:
                        next.append(now)
                    else:
                        next.appendleft(now)
                    rc_info[now] = (nr, nc)
                while next:
                    pieces[nr][nc].append(next.pop())
                if len(pieces[nr][nc]) >= 4:
                    return turn

    return -1


print(main())
