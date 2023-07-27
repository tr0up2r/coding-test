from collections import deque


def solution(queue1, queue2):
    answer = 0
    goal = sum(queue1) + sum(queue2)
    len_queue = len(queue1)
    queue1, queue2 = deque(queue1), deque(queue2)

    sum1, sum2 = sum(queue1), sum(queue2)

    if goal % 2 == 1:
        return -1

    while sum1 != sum2:
        answer += 1
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp

        if answer > len_queue * 4:
            answer = -1
            break

    return answer
