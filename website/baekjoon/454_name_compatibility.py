s = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()
l = []

for a, b in zip(A, B):
    l.extend([s[ord(a)-ord('A')], s[ord(b)-ord('A')]])
for i in range(len(l)-1, 1, -1):
    for j in range(0, i):
        l[j] = (l[j]+l[j+1])%10
print(''.join(list(map(str, l[:2]))))
