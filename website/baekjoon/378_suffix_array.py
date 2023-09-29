s = input()
for x in sorted([s[i:] for i in range(len(s))]):
    print(x)
