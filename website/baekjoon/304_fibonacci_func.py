t = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1
for i in range(2, 41):
    for j in range(2):
        dp[i][j] = dp[i-2][j] + dp[i-1][j]

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])
