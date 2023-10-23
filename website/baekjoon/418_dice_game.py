sa, sb = 100, 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        sb -= a
    elif a < b:
        sa -= b
print(f'{sa}\n{sb}')
