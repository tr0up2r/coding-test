n = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

now = 1e9
result = 0

for i in range(n - 1):
    now = min(now, cities[i])
    result += distances[i] * now

print(result)
