# 행의 개수 n, 열의 개수 m
# 숫자 입력은 1 이상 10,000 이하의 자연수

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)
