n, k = map(int, input().split())
data = list(map(int, input().split()))
l, r = 0, k
now = sum(data[:r])
answer = now

while r < n:
    now = now - data[l] + data[r]
    answer = max(answer, now)
    l += 1
    r += 1

print(answer)
