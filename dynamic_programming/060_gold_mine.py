import sys
input = sys.stdin.readline

result = []

# t: 테스트 케이스
for t in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            left = -1e9
            left_up = -1e9
            left_down = -1e9
            # dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]
            left = dp[i][j-1]
            if i-1 >= 0:
                left_up = dp[i-1][j-1]
            if i+1 < n:
                left_down = dp[i+1][j-1]
            dp[i][j] += max(left, left_up, left_down)

    result.append(max(map(max, dp)))

for r in result:
    print(r)


"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
