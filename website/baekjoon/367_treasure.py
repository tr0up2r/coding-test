n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
s = 0
for a, b in zip(A, B):
    s += a*b
print(s)
