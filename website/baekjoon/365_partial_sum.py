n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r, now = 0, 0, 0
min_l = 100001

while True:
    if now >= s:
        min_l = min(min_l, r-l)
        now -= arr[l]
        l += 1
    elif r == n:
        break
    else:
        now += arr[r]
        r += 1

print(min_l if min_l <= n else 0)
