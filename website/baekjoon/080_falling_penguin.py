n = int(input())
data = list(map(int, input().split()))
i = data.index(-1)
print(min(data[:i]) + min(data[i+1:]))
