n, k = map(int, input().split())
stuff = [[0, 0]]
dp = [[0]*(k+1) for _ in range(n+1)]
for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = stuff[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])
print(dp[n][k])
