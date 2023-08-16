from collections import Counter


n = int(input())
data, answer = [], []
for _ in range(n):
    data.append(input()[0])

for k, v in Counter(data).most_common():
    if v < 5:
        break
    answer.append(k)

print(''.join(sorted(answer)) if answer else 'PREDAJA')
