n = int(input())
print('SK' if n % 2 else 'CY')

'''
dp = [0] * 1001
dp[1], dp[3] = 1, 1

for i in range(2, n+1):
    if dp[i] == 0:
        if i % 3 == 0:
            dp[i] = dp[3 * ((i-1)//3)] + 1
        else:
            dp[i] = dp[i-1] + 1

print('SK' if dp[n] % 2 else 'CY')
'''
