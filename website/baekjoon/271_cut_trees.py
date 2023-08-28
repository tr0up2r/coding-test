n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    cut_sum = 0
    for tree in arr:
        cut_sum += max(tree-mid, 0)

    if cut_sum >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
