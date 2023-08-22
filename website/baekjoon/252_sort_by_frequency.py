n, c = map(int, input().split())
m = list(map(int, input().split()))
d = dict()

now = 0
for i in m:
    if i not in d:
        d[i] = [now, 1]
        now += 1
    else:
        d[i][1] += 1

count = sorted(d.items(), key=lambda x: (-x[1][1], x[1][0]))

for num, info in count:
    for _ in range(info[1]):
        print(num, end=' ')
