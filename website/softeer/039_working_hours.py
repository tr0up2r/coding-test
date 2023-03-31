import sys
input = sys.stdin.readline

work_time = []


def get_time(t):
    return int(t.split(':')[0])*60 + int(t.split(':')[1])


for _ in range(5):
    a, b = input().split()
    work_time.append(get_time(b) - get_time(a))

print(sum(work_time))
