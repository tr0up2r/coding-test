n, k = map(int, input().split())
arr = list(map(int, input().split()))
l, r, answer, counts = 0, 0, 0, [0]*100001

while r < n:
    if counts[arr[r]] >= k:
        counts[arr[l]] -= 1
        l += 1
    else:
        counts[arr[r]] += 1
        r += 1
    answer = max(answer, r-l)

print(answer)
