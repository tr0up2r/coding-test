from collections import deque


def solution(order):
    answer = 0
    main, sub = deque([num for num in range(1, len(order) + 1)]), deque([])

    for o in order:
        while True:
            if sub:
                if o == sub[-1]:
                    sub.pop()
                    answer += 1
                    break
            if not main:
                return answer
            sub.append(main.popleft())

    return answer
