s = list(input())
count_0 = s.count('0') // 2
count_1 = s.count('1') // 2

for _ in range(count_1):
    s.pop(s.index('1'))
for _ in range(count_0):
    s.pop(-s[::-1].index('0')-1)

print(''.join(s))
