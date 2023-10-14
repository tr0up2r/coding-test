import copy


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blocks, values = [], dict()
for r in range(n):
    for c in range(n):
        if arr[r][c]:
            blocks.append((r, c))
            values[(r, c)] = arr[r][c]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_block = -1e9


def dfs(blocks, values, depth):
    if depth == 5:
        global max_block
        max_block = max(max_block, max(values.values()))
        return

    for i in range(4):
        visited = [[False]*n for _ in range(n)]
        new_blocks = []
        new_values = copy.deepcopy(values)
        if i == 0:
            blocks.sort(key=lambda x: x[0])
        elif i == 1:
            blocks.sort(key=lambda x: -x[0])
        elif i == 2:
            blocks.sort(key=lambda x: x[1])
        else:
            blocks.sort(key=lambda x: -x[1])

        for j in range(len(blocks)):
            end = False
            r, c = blocks[j]
            nr, nc = r, c
            while True:
                nr, nc = nr+dr[i], nc+dc[i]
                if not (0 <= nr < n and 0 <= nc < n):
                    end = True
                    break
                else:
                    if (nr, nc) in new_values and new_values[(nr, nc)] != 0:
                        break
            if not end and new_values[(nr, nc)] == new_values[(r, c)] and not visited[nr][nc]:
                new_values[(nr, nc)] *= 2
                new_values[(r, c)] = 0
                visited[nr][nc] = True
            else:
                nr, nc = nr-dr[i], nc-dc[i]
                if nr != r or nc != c:
                    new_values[(nr, nc)], new_values[(r, c)] = new_values[(r, c)], 0
                new_blocks.append((nr, nc))

        dfs(new_blocks, new_values, depth+1)


dfs(blocks, values, 0)
print(max_block)
