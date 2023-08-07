cost = list(map(int, input().split()))
d = dict()
for i in range(3):
    d[i+1] = cost[i]

data = [0] * 100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start-1, end-1):
        data[i] += 1

for i in range(len(data)):
    if data[i] == 0:
        continue
    data[i] *= d[data[i]]

print(sum(data))
