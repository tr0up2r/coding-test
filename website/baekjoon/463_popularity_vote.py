n = int(input())
l = list(input().split())
d = {s: 0 for s in l}
for _ in range(n):
    likes = list(input().split())
    for like in likes:
        d[like] += 1
students = sorted(d, key=lambda x: d[x], reverse=True)
for s in students:
    print(s, d[s])
