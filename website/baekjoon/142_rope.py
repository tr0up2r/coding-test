n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)

result = -1e9
for i in range(len(data)):
    result = max(result, data[i] * (i + 1))

print(result)
