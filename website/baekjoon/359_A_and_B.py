s = input()
t = input()
flag = 0


def dfs(now):
    global flag
    if now == s:
        flag = 1
        return
    if len(now) == 0:
        return

    if now[-1] == 'A':
        dfs(now[:-1])
    if now[-1] == 'B':
        dfs(now[:-1][::-1])


dfs(t)
print(flag)
