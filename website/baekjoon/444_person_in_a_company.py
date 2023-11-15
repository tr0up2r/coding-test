s = set()
for _ in range(int(input())):
    name, op = input().split()
    if op == 'enter':
        s.add(name)
    else:
        s.remove(name)
for e in sorted(s, reverse=True):
    print(e)
