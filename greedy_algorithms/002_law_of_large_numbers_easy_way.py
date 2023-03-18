# 배열의 크기 n, 숫자가 더해지는 횟수 m (1 <= M <= 10,000), 연속해서 더해질 수 있는 횟수 k

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
