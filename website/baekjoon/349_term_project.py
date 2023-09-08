import sys
sys.setrecursionlimit(100000)


def dfs(now, l):
    if arr[now][0] in checked:
        idx = l.index(arr[now][0])
        for s in l[idx:]:
            arr[s][1] = 1
        return

    if not visited[arr[now][0]] and not arr[now][1]:
        visited[arr[now][0]] = 1
        l.append(arr[now][0])
        checked.add(arr[now][0])
        dfs(arr[now][0], l)
        l.pop()


for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    arr = [[]]
    for i, like in enumerate(data):
        arr.append([like, 0])
    visited = [0]*(n+1)
    for i in range(1, n+1):
        if not visited[i] and not arr[i][1]:
            checked = set([i])
            dfs(i, [i])

    answer = 0

    for i in range(1, n+1):
        if not arr[i][1]:
            answer += 1
    print(answer)
