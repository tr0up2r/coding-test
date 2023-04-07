class Player:
    def __init__(self, num, x, y, d, s):
        self.num, self.x, self.y, self.d, self.s = num, x, y, d, s
        self.gun = 0
        self.point = 0
        players_idxs[num] = (x, y)

    def go_straight(self, mode):
        if mode == 'normal':
            nx = self.x + dx[self.d]
            ny = self.y + dy[self.d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                self.d = (self.d+2)%4
                nx = self.x + dx[self.d]
                ny = self.y + dy[self.d]
            self.x, self.y = nx, ny
        else:  # mode == 'lose'
            while True:
                nx = self.x + dx[self.d]
                ny = self.y + dy[self.d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in players_idxs.values():
                    self.d = (self.d+1)%4
                    continue
                self.x, self.y = nx, ny
                break

    def get_xy(self):
        return self.x, self.y

    def get_power(self):
        return self.s, self.s + self.gun  # 초기 능력치 & 초기 능력치 + 총 비교

    def get_gun(self):
        return self.gun

    def get_point(self):
        return self.point

    def set_point(self, new_point):
        self.point += new_point

    def set_gun(self, gun):
        self.gun = gun

    def take_gun(self):
        if not data[self.x][self.y]:  # 총이 없으면 종료
            return
        max_gun = self.gun
        now_gun = self.gun
        for gun in data[self.x][self.y]:
            max_gun = max(max_gun, gun)
        if max_gun == self.gun:  # 지금 총이 가장 센 총이라면 종료
            return
        self.gun = data[self.x][self.y].pop(data[self.x][self.y].index(max_gun))
        if now_gun == 0:  # 0은 내려놓지 않기
            return
        data[self.x][self.y].append(now_gun)

    def print_status(self):  # 테스트용
        if self.d == 0:
            d = 'up'
        elif self.d == 1:
            d = 'right'
        elif self.d == 2:
            d = 'down'
        else:
            d = 'left'
        print(f'Player {self.num} ({d})\n({self.x},{self.y}), gun: {self.gun}, power: {self.s}+{self.gun}, s: {self.s}, point: {self.point}')


def strife(i, j):  # i번째 플레이어와 j번째 플레이어 싸움
    # print(f'strife! {i} vs {j} at {players[i].get_xy()}')
    s1, power1 = players[i].get_power()
    s2, power2 = players[j].get_power()

    if power1 > power2:
        players[i].set_point(power1-power2)
        winner, loser = i, j
    elif power1 < power2:
        players[j].set_point(power2-power1)
        winner, loser = j, i
    else:  # 동점일 경우
        if s1 > s2:
            winner, loser = i, j
        else:
            winner, loser = j, i
    return winner, loser  # 이긴 사람, 진 사람 순서대로 return하여 다음 동작 수행


def move_of_loser(i):
    x, y = players[i].get_xy()
    gun = players[i].get_gun()
    if gun > 0:
        data[x][y].append(gun)
        players[i].set_gun(0)  # 총 바닥에 버리기
    players[i].go_straight('lose')
    x, y = players[i].get_xy()
    players_idxs[i] = (x, y)
    players[i].take_gun()


def print_point():
    for player in players:
        print(player.get_point(), end=' ')


# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())  # n: 격자 크기, m: 플레이어 수, k: 라운드 수
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            data[i][j] = []
        else:
            data[i][j] = [data[i][j]]

players = []
players_idxs = {}
for i in range(m):
    x, y, d, s = map(int, input().split())
    players.append(Player(i, x-1, y-1, d, s))

for _ in range(k):  # 라운드 수 동안 진행
    for i in range(len(players)):
        fight_flag = False
        x, y = players[i].get_xy()
        players[i].go_straight('normal')
        x, y = players[i].get_xy()
        players_idxs[i] = (x, y)
        for key in players_idxs.keys():
            if players[i].get_xy() == players_idxs[key] and key != i:  # 이동한 방향에 플레이어가 있는지 확인
                winner, loser = strife(i, key)
                move_of_loser(loser)
                players[winner].take_gun()
                fight_flag = True
                break
        if fight_flag:  # 싸움이 일어났으면 다음 반복으로
            continue
        else:  # 이동한 방향에 플레이어가 없다면 총이 있는지 확인
            players[i].take_gun()

print_point()
