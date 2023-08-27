n = int(input())
arr = list(map(int, input().split()))
m = int(input())

if sum(arr) <= m:
    print(max(arr))
else:
    start, end, mid = 0, m, m//2

    while start != mid:
        new_arr = list(map(lambda x: min(mid, x), arr))
        if sum(new_arr) > m:
            end = mid
            mid = (start + end) // 2
        elif sum(new_arr) < m:
            start = mid
            mid = (start + end) // 2
        else:
            break
    print(mid)
