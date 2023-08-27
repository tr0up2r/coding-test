n, x = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, x
max_v, now_v, max_c = sum(arr[:end]), sum(arr[:end]), 1

while True:
    if end == n:
        break
    now_v = now_v - arr[start] + arr[end]
    if now_v > max_v:
        max_v = now_v
        max_c = 1
    elif now_v == max_v:
        max_c += 1
    start += 1
    end += 1

if max_v:
    print(max_v)
    print(max_c)
else:
    print("SAD")
