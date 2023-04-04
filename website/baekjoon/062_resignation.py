import sys
input = sys.stdin.readline

n = int(input())  # 전체 상담 개수
t = []  # 각 상담을 완료하는 데 걸리는 기간
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i]+i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)