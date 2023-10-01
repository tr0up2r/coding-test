d = dict()
t_count = 0

while True:
    try:
        s = input()
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
        t_count += 1
    except EOFError:
        break

for tree in sorted(d.keys()):
    print(f'{tree} {d[tree]/t_count*100:.4f}')
