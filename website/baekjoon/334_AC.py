from collections import deque


for _ in range(int(input())):
    p = input()
    n = int(input())
    x = input()
    x = deque(x[1:len(x)-1].split(',')) if len(x) > 2 else deque()
    r_flag = 0
    e_flag = 0

    for i in p:
        if i == 'R':
            r_flag = 1-r_flag
        else:
            if not x:
                e_flag = 1
                break
            if r_flag:
                x.pop()
            else:
                x.popleft()

    if not e_flag:
        answer = '['
        if r_flag:
            x.reverse()
        for i in range(len(x)):
            if i == len(x)-1:
                answer += x[i]
            else:
                answer += x[i] + ','
        answer += ']'
        print(answer)
    else:
        print('error')
