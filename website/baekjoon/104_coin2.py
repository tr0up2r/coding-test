n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1e9] * 10001

for c in coins:
    if c > 10000:
        continue
    dp[c] = 1
dp[0] = 0
for i in range(1, 10001):
    for c in coins:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])
