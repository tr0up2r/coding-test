game = {'Y': 1, 'F': 2, 'O': 3}

n, g = input().split()
s = set()
now, answer = 0, 0
for _ in range(int(n)):
    name = input()
    if name not in s:
        s.add(name)
        now += 1
        if now == game[g]:
            answer += 1
            now = 0

print(answer)
