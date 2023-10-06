n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for r in range(1, n+1):
    for c in range(1, m+1):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])+arr[r-1][c-1]

print(dp[n][m])
