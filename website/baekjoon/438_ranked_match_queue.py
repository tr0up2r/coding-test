p, m = map(int, input().split())
arr = [[] for _ in range(p)]
for _ in range(p):
    l, n = input().split()
    l = int(l)
    for i in range(p):
        if not arr[i] or (arr[i][0][0]-10 <= l <= arr[i][0][0]+10 and len(arr[i]) < m):
            arr[i].append((l, n))
            break
for a in arr:
    if a:
        if len(a) == m:
            print('Started!')
        else:
            print('Waiting!')
        a.sort(key=lambda x: x[1])
        for l, n in a:
            print(l, n)
