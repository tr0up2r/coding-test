arr = [[[] for _ in range(4)] for _ in range(4)]
baby = [[[] for _ in range(4)] for _ in range(4)]
dead = [[[] for _ in range(4)] for _ in range(4)]

m, t = map(int, input().split())
pr, pc = map(int, input().split())
pr -= 1
pc -= 1
for _ in range(m):
    r, c, d = map(int, input().split())
    arr[r-1][c-1].append(d-1)

# 상 좌 하 우
dr4 = [-1, 0, 1, 0]
dc4 = [0, -1, 0, 1]

dr8 = [-1, -1, 0, 1, 1, 1, 0, -1]
dc8 = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(arr, r, c, count, eat, dirs):
    if count == 3:
        global poss, now
        poss.append((eat, now, dirs[:]))
        now += 1
        return

    for i in range(4):
        nr, nc = r+dr4[i], c+dc4[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            num_mon = len(arr[nr][nc])
            tmp = arr[nr][nc][:]
            arr[nr][nc].clear()
            eat += num_mon
            dirs.append(i)
            dfs(arr, nr, nc, count+1, eat, dirs)
            dirs.pop()
            eat -= num_mon
            for d in tmp:
                arr[nr][nc].append(d)


while t:
    move_list = []
    for r in range(4):
        for c in range(4):
            while arr[r][c]:
                d = arr[r][c].pop()
                # 1. 몬스터 복제 시도
                baby[r][c].append(d)
                # 2-1. 몬스터 이동 리스트 구하기
                flag = False
                for i in range(8):
                    nd = (d+i)%8
                    nr, nc = r+dr8[nd], c+dc8[nd]
                    if 0 <= nr < 4 and 0 <= nc < 4 and not dead[nr][nc] and not (nr == pr and nc == pc):
                        move_list.append((nr, nc, nd))
                        flag = True
                        break
                if not flag:
                    move_list.append((r, c, d))
    # 2-2. 몬스터 이동
    for r, c, d in move_list:
        arr[r][c].append(d)

    # 3-1. 팩맨 이동 경로 찾기
    poss, now = [], 0
    dfs(arr, pr, pc, 0, 0, [])
    poss.sort(key=lambda a: (-a[0], a[1]))
    route = poss[0][2]
    for d in route:
        pr, pc = pr+dr4[d], pc+dc4[d]
        # 3-2. 몬스터 먹기 + 시체 생성
        for _ in range(len(arr[pr][pc])):
            dead[pr][pc].append(3)
        arr[pr][pc].clear()

    # 4. 몬스터 시체 소멸 + 5. 몬스터 복제 완성
    for r in range(4):
        for c in range(4):
            erase = 1e9
            for i in range(len(dead[r][c])):
                dead[r][c][i] -= 1
                if dead[r][c][i] == 0:
                    erase = i
            if erase < 1e9:
                dead[r][c] = dead[r][c][erase+1:]
            while baby[r][c]:
                arr[r][c].append(baby[r][c].pop())

    t -= 1

answer = 0
for r in range(4):
    for c in range(4):
        answer += len(arr[r][c])
print(answer)
