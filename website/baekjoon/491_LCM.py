A, B = map(int, input().split())
a, b = A, B
while a%b:
    a, b = b, a%b
print((A*B)//b)
