n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

now = (arr[0][1], arr[0][2], arr[0][3])
rank, i = 1, 0
for num, g, s, b in arr:
    i += 1
    if (g, s, b) != now:
        rank = i
        now = (g, s, b)
    if num == k:
        print(rank)
        break
