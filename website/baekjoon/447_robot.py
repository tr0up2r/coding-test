R, C = map(int, input().split())
arr = [['*']*C for _ in range(R)]
for _ in range(int(input())):
    br, bc = map(int, input().split())
    arr[br][bc] = 'x'
sr, sc = map(int, input().split())
arr[sr][sc] = 0
ds = list(map(lambda x: int(x)-1, input().split()))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = 0

while True:
    flag = True
    for i in range(4):
        nd = (d+i)%4
        nr, nc = sr+dr[ds[nd]], sc+dc[ds[nd]]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == '*':
            arr[nr][nc] = arr[sr][sc]+1
            sr, sc, d = nr, nc, nd
            flag = False
            break
    if flag:
        break
print(sr, sc)
