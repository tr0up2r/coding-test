dp = [0]*1000001
dp[1], dp[2] = 1, 2
for i in range(3, 1000001):
    dp[i] = (dp[i-2]+dp[i-1])%15746
print(dp[int(input())])
