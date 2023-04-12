n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for c in coins:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]

print(dp[k])
