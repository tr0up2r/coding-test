x = int(input())
y = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    y += a*b
print('Yes') if x == y else print('No')
