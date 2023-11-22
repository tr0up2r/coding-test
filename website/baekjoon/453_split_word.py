s = input()
res = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        res.append(''.join(list(map(lambda x: x[::-1], [s[0:i], s[i:j], s[j:]]))))
print(sorted(res)[0])
