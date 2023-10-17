n, m = map(int, input().split())
arr = list(range(n+1))
for _ in range(m):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]
print(*arr[1:])
