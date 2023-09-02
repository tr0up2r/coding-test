import sys


m = int(input())


# 입력 숫자 범위가 좁다는 것을 이용한 풀이
# 4188ms
def func1(m):
    s = [0] * 21
    for _ in range(m):
        op = sys.stdin.readline().rstrip()
        if len(op.split()) == 2:
            op, x = op.split()
            x = int(x)
        if op == 'add':
            s[x] = 1
        elif op == 'remove':
            s[x] = 0
        elif op == 'check':
            print(1 if s[x] else 0)
        elif op == 'toggle':
            s[x] = 0 if s[x] else 1
        else:
            s.clear()
            if op == 'all':
                s = [1] * 21
            else:
                s = [0] * 21


# set을 활용한 정석 풀이
# 4444ms
def func2(m):
    s = set()
    for _ in range(m):
        op = sys.stdin.readline().rstrip()
        if len(op.split()) == 2:
            op, x = op.split()
            x = int(x)
        if op == 'add':
            s.add(x)
        elif op == 'remove':
            s.discard(x)
        elif op == 'check':
            print(1 if x in s else 0)
        elif op == 'toggle':
            s.discard(x) if x in s else s.add(x)
        elif op == 'all':
            s.clear()
            s = set(list(range(1, 21)))
        else:
            s.clear()


func1(m)
# func2(m)
