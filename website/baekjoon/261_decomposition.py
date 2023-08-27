n = int(input())
m = 1
while m < n:
    if n == (m + sum([int(n) for n in str(m)])):
        break
    m += 1

print(0 if n == m else m)
