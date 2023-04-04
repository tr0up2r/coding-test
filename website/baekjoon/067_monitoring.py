n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0
for room in a:
    room -= b
    count += 1
    if room <= 0:
        continue
    mod = 0
    if room % c:
        mod = 1
    count += int(room / c) + mod
print(count)
