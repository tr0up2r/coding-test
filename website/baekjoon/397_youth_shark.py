import copy


arr = []
for _ in range(4):
    now = list(map(int, input().split()))
    l = []
    for i in range(0, 7, 2):
        l.append([now[i], now[i+1]-1])
    arr.append(l)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
answer = -1e9


def dfs(sr, sc, arr, now):
    now += arr[sr][sc][0]
    global answer
    answer = max(answer, now)
    arr[sr][sc][0] = 0
    shark = arr[sr][sc]

    for i in range(1, 17):
        fr, fc = -1, -1
        for r in range(4):
            for c in range(4):
                if arr[r][c][0] == i:
                    fr, fc = r, c
                    break
        if fr == -1 and fc == -1:
            continue

        turn = 8
        while turn:
            nr, nc = fr+dr[arr[fr][fc][1]], fc+dc[arr[fr][fc][1]]
            if 0 <= nr < 4 and 0 <= nc < 4 and arr[nr][nc][0] != 0:
                arr[fr][fc], arr[nr][nc] = arr[nr][nc], arr[fr][fc]
                break
            else:
                arr[fr][fc][1] = (arr[fr][fc][1]+1)%8
                turn -= 1

    for i in range(1, 4):
        nsr, nsc = sr+(dr[arr[sr][sc][1]]*i), sc+(dc[arr[sr][sc][1]]*i)
        if 0 <= nsr < 4 and 0 <= nsc < 4 and arr[nsr][nsc][0] != -1:
            arr[sr][sc] = [-1, -1]
            dfs(nsr, nsc, copy.deepcopy(arr), now)
            arr[sr][sc] = shark


dfs(0, 0, arr, 0)
print(answer)
