h, w = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(1, w-1):
    min_rain = 0
    left = max(data[:i])
    right = max(data[i+1:])
    min_rain = min(left, right)

    if data[i] < min_rain:
        result += min_rain - data[i]

print(result)
