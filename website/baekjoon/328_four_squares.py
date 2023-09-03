n = int(input())
dp = [1e9] * 50001
dp[0] = 0

for i in range(1, n+1):
    root = int(i**(1/2))
    while root:
        dp[i] = min(1+dp[i-(root**2)], dp[i])
        root -= 1

print(dp[n])
