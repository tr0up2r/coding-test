s = input()
counts = [0] * (ord('z') - ord('a') + 1)

for a in s:
    counts[ord(a)-ord('a')] += 1

for c in counts:
    print(c, end=' ')
