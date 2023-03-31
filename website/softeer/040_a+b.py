import sys
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    a, b = map(int, input().split())
    result.append(a+b)

for i in range(0, t):
    print(f'Case #{i+1}: {result[i]}')
