n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

idxs = [i for i in range(n)]
visited = [False] * n
comb_list = []
comb_size = n // 2


def dfs(idx, now_list):
    if len(now_list) == comb_size:
        comb_list.append(now_list[:])

    for i in range(idx, n):
        dfs(i+1, now_list+[idxs[i]])


# make comb list
dfs(0, [])

min_value = 1e9
for i in range(len(comb_list) // 2):
    start_comb = comb_list[i]
    link_comb = comb_list[len(comb_list)-1-i]

    start = 0
    link = 0
    for j in range(len(start_comb)-1):
        for k in range(j+1, len(start_comb)):
            start += data[start_comb[j]][start_comb[k]] + data[start_comb[k]][start_comb[j]]
            link += data[link_comb[j]][link_comb[k]] + data[link_comb[k]][link_comb[j]]
    min_value = min(min_value, abs(start-link))

print(min_value)
