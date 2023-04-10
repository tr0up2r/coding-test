a, b = map(int, input().split())
A, B, gcd = a, b, b
while a % gcd:
    a, gcd = gcd, a%gcd
lcm = A*B//gcd

print(gcd)
print(lcm)
