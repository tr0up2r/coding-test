n, m = map(int, input().split())
data = []
chicken_idx = []
chicken_count = 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2:
            chicken_idx.append((i, j))
            chicken_count += 1
    data.append(line)


def get_perm(idx, now_list):
    if len(now_list) == m:
        chicken_perm.append(now_list[:])
    for i in range(idx, chicken_count):
        get_perm(i+1, now_list+[chicken_idx[i]])


chicken_perm = []
if chicken_count > m:
    get_perm(0, [])


def get_min_distance(house_xy, chicken_xys):
    md = 1e9
    for xy in chicken_xys:
        d = abs(house_xy[0] - xy[0]) + abs(house_xy[1] - xy[1])
        md = min(md, d)
    return md


min_distance = 1e9
if chicken_perm:
    for perm in chicken_perm:
        distance = 0
        for i in range(n):
            for j in range(n):
                if data[i][j] == 1:
                    distance += get_min_distance((i, j), perm)
        min_distance = min(min_distance, distance)
    print(min_distance)
else:
    distance = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                distance += get_min_distance((i, j), chicken_idx)
    print(distance)
