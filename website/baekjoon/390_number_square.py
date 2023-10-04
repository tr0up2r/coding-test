n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]


def find_biggest(n, m):
    min_l = min(n, m)-1
    while min_l:
        for r in range(n-min_l):
            nr = r+min_l
            for c in range(m-min_l):
                nc = c+min_l
                if arr[r][c] == arr[nr][c] == arr[r][nc] == arr[nr][nc]:
                    return (min_l+1)**2
        min_l -= 1
    return 1


print(find_biggest(n, m))
