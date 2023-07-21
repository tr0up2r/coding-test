n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
result = 0
for i in range(len(data)):
    if data[i] - i <= 0:
        break
    result += data[i] - i

print(result)
