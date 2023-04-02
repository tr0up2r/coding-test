import sys
input = sys.stdin.readline

n, m = map(int, input().split())

standards = [0] * 100
real = [0] * 100
subs = [0] * 100


def make_dv_array(array, n):
    i = 0
    for _ in range(n):
        d, v = map(int, input().split())
        d += i
        while i < d:
            array[i] = v
            i += 1
    return array


standards = make_dv_array(standards, n)
real = make_dv_array(real, m)

biggest = 0
for i in range(len(standards)):
    biggest = max(biggest, real[i] - standards[i])

print(biggest)
