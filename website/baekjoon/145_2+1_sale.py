n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
result = sum(data)
for i in range(2, n, 3):
    result -= data[i]

print(result)
