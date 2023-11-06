ans, s = 0, set()
for _ in range(int(input())):
    now = input()
    if now == 'ENTER':
        ans += len(s)
        s = set()
    else:
        s.add(now)
print(ans+len(s))
