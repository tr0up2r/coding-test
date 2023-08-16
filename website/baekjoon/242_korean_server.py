import re


n = int(input())
pattern = input().replace('*', '.*')
p = re.compile(pattern)

for _ in range(n):
    t = input()
    if t == ''.join(pattern.split('.*')):
        print('DA')
    else:
        if p.fullmatch(t):
            print('DA')
        else:
            print('NE')
