import sys
input = sys.stdin.readline

# a: 고정 비용, b: 가변 비용, c: 하나 가격
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print((a // (c-b))+1)
