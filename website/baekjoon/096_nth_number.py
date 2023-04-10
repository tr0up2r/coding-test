t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    data.sort()
    print(data[len(data)-3])
    data.clear()
