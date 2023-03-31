import sys
input = sys.stdin.readline

data = list(map(int, input().split()))


def solution(data):
    last = data[0]
    if last == 1:
        result = 'ascending'
    elif last == 8:
        result = 'descending'
    else:
        result = 'mixed'

    for d in data[1:]:
        if result == 'ascending' and d == last+1:
            last = d
        elif result == 'descending' and d == last-1:
            last = d
        else:
            return 'mixed'

    return result


print(solution(data))
