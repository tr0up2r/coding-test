# 어떤 수 n이 1이 될 때까지,
# N에서 1을 빼거나 N을 K로 나누기
# 횟수를 최소화 하기

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k:
        n -= 1
    else:
        n //= k
    count += 1

print(count)
