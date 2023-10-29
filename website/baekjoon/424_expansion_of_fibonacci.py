N = 1000000
dp = [0]*(2*N+1)
dp[N+1], dp[N-1] = 1, 1
for i in range(2, N+1):
    dp[N+i] = (dp[N+i-1]+dp[N+i-2])%1000000000
    dp[N-i] = (dp[N-i+2]-dp[N-i+1])
    if dp[N-i] < 0:
        sign = -1
        dp[N-i] *= -1
    else:
        sign = 1
    dp[N-i] = (dp[N-i]%1000000000)*sign

n = int(input())
if dp[N+n] > 0:
    print(1)
elif dp[N+n] == 0:
    print(0)
else:
    print(-1)
print(abs(dp[N+n]))
