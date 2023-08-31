n = int(input())
answer = []


def stack_seq():
    global answer
    stack = []
    now = 1

    for _ in range(n):
        num = int(input())
        while now <= num:
            stack.append(now)
            now += 1
            answer.append('+')
        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            return False
    return True


if stack_seq():
    for s in answer:
        print(s)
else:
    print('NO')
