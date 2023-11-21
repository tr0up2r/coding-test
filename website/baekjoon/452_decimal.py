a, b, n = map(int, input().split())
while n:
    a = (a%b)*10
    n -= 1
print(a//b)
