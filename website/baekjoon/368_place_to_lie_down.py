n = int(input())
arr = [list(input()) for _ in range(n)]
answer = [0, 0]

for i in range(n):
    r, c = 0, 0
    for j in range(n):
        if arr[i][j] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            answer[0] += 1

        if arr[j][i] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            answer[1] += 1

print(*answer)
