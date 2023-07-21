n, m = map(int, input().split())
j = int(input())

now = list(range(1, m + 1))
result = 0

for _ in range(j):
    apple = int(input())
    while True:
        if apple in now:
            break
        else:
            if apple > max(now):
                now = list(map(lambda x: x + 1, now))
            else:
                now = list(map(lambda x: x - 1, now))
            result += 1

print(result)
