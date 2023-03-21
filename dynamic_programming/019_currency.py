n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# dp[i]가 10001이면 그 값은 주어진 화폐로 만들 수 없다는 뜻
# 다른 수라면 i를 만들기 위해 쓰이는 화폐 수를 dp[i]에 기록
dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if dp[j - array[i]] != 10001:
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
