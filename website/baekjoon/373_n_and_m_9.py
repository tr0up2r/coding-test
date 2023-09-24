n, m = map(int, input().split())
arr = sorted(map(int, list(input().split())))
visited = [0]*n
s = set()


def dfs(now, count):
    if count == m and now not in s:
        s.add(now)
        print(now)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            tmp = f'{now} {arr[i]}'
            dfs(tmp, count+1)
            visited[i] = 0
    return


for i in range(len(arr)):
    visited[i] = 1
    dfs(str(arr[i]), 1)
    visited[i] = 0
