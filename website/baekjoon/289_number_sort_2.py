n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def merge(start, end):
    mid = (start + end) // 2
    res = []
    l, r = start, mid+1

    while l <= mid and r <= end:
        if arr[l] <= arr[r]:
            res.append(arr[l])
            l += 1
        else:
            res.append(arr[r])
            r += 1

    res += arr[l:mid+1]
    res += arr[r:end+1]

    for i in range(start, end+1):
        arr[i] = res[i-start]


def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, end)


merge_sort(0, len(arr)-1)
for n in arr:
    print(n)
