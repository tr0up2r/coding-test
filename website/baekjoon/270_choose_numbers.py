n = int(input())
data = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data[int(input())].append(i)

answer = []
checked = [False] * (n+1)


def dfs(idx, visited):
    checked[idx] = True
    visited.add(idx)
    for v in data[idx]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            answer.extend(list(visited))


for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set())

answer.sort()
print(len(answer))
for v in answer:
    print(v)
