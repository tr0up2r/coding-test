max_people = -1e9
count = 0
for _ in range(10):
    a, b = map(int, input().split())
    count -= a
    max_people = max(max_people, count)
    count += b
    max_people = max(max_people, count)
print(max_people)
