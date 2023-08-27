n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

for now in arr:
    rank = 1
    for other in arr:
        if now[0] < other[0] and now[1] < other[1]:
            rank += 1
    print(rank, end=' ')
