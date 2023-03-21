n = int(input())
array = list(map(int, input().split()))

# i번째까지 창고가 존재한다고 했을 때, 최적값이 d[i]에 저장됨.
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])
