k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    print(start, mid, end)
    now = sum(list(map(lambda x: x//mid, arr)))
    if now < n:
        end = mid-1
    else:
        start = mid+1
    print(start, mid, end)
    print('===========')

print(end)
