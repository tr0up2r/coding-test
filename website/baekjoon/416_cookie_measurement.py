n = int(input())
arr = [list(input()) for _ in range(n)]
answer = [0, 0, 0, 1, 1]
dr = [0, 0, 1]
dc = [-1, 1, 0]


def get_length(ai, d, r, c):
    nr, nc = r, c
    while True:
        nr, nc = nr+dr[d], nc+dc[d]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == '*':
            answer[ai] += 1
        else:
            break


def main():
    for r in range(1, n-1):
        for c in range(1, n-1):
            if arr[r-1][c] == '*' and arr[r+1][c] == '*' and arr[r][c-1] == '*' and arr[r][c+1] == '*':
                print(r+1, c+1)
                get_length(0, 0, r, c)
                get_length(1, 1, r, c)
                get_length(2, 2, r, c)
            elif arr[r+1][c] == '_' and arr[r+1][c-1] == '*' and arr[r+1][c+1] == '*':
                get_length(3, 2, r+1, c-1)
                get_length(4, 2, r+1, c+1)
                return


main()
print(*answer)
