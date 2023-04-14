from itertools import combinations

n = int(input())
answer = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        answer.append(int(''.join(sorted(map(str, list(j)), reverse=True))))

answer.sort()
print(-1 if n >= len(answer) else answer[n])
