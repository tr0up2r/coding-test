n = int(input())
arr = list(map(int, input().split()))
s = sorted(list(set(arr)))
d = {x: i for i, x in enumerate(s)}

for x in arr:
    print(d[x], end=' ')
