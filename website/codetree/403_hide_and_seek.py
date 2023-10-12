from collections import deque


n, m, h, k = map(int, input().split())
tr, tc, td, tcount, cw = n//2, n//2, 0, 0, 1
remain = tcount//2+1
runners = deque()

for _ in range(m):
    r, c, d = map(int, input().split())
    runners.append((r-1, c-1, d))

trees = set()
for _ in range(h):
    r, c = map(int, input().split())
    trees.add((r-1, c-1))

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def runner_move(r, c, d):
    nr, nc = r+dr[d], c+dc[d]
    if 0 <= nr < n and 0 <= nc < n:  # 격자 벗어나지 않는다면
        if nr != tr or nc != tc:  # 가려는 곳에 술래만 없으면 go
            return True, (nr, nc, d)
        else:
            return True, (r, c, d)
    else:
        return False, (0, 0)


turn, answer = 1, 0
while turn <= k:
    # 1. 도망자 움직이기
    n_runners = len(runners)
    for _ in range(n_runners):
        r, c, d = runners.popleft()
        # 1-1. 술래와의 거리 3 이하이면 움직이기
        if abs(tr-r)+abs(tc-c) <= 3:
            flag, new_rcd = runner_move(r, c, d)
            # 1-2. 격자 벗어나면 방향 반대로 틀기
            if not flag:
                d = (d+2)%4
                _, new_rcd = runner_move(r, c, d)
            runners.append(new_rcd)
        else:
            runners.append((r, c, d))

    # 2. 술래 움직이기 (달팽이 회전)
    if not (0 <= tr+dr[td] < n and 0 <= tc+dc[td] < n):
        cw *= -1
        remain = tcount//2+1
        remain -= 1
        td = (td+2)%4

    tr, tc = tr+dr[td], tc+dc[td]
    if tr == n//2 and tc == n//2:
        td, tcount, cw = 0, 0, 1
        remain = tcount//2+1
    else:
        remain -= 1
        if not remain:
            if cw == 1:
                td = (td+1)%4
                tcount += 1
            else:
                td = (td-1)%4
                tcount -= 1
            remain = tcount//2+1

    # 3. 도망자 잡기
    new_runners, catch = [], 0
    for rr, rc, d in runners:
        cr, cc = tr, tc
        flag = True
        for i in range(3):
            cr, cc = tr+(dr[td]*i), tc+(dc[td]*i)
            if 0 <= cr < n and 0 <= cc < n:
                if (cr, cc) == (rr, rc) and (rr, rc) not in trees:
                    flag = False
                    catch += 1
                    break
        if flag:
            new_runners.append((rr, rc, d))

    answer += turn*catch
    runners = deque(new_runners)
    turn += 1

print(answer)
