board = [[0]*8 for _ in range(8)]
king, stone, n = input().split()


def get_rc(pos):
    return [7-(int(pos[1])-1), ord(pos[0])-ord('A')]


def get_pos(rc):
    return chr(ord('A')+rc[1])+str(7-rc[0]+1)


k_rc = get_rc(king)
s_rc = get_rc(stone)
d = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0]}

for _ in range(int(n)):
    move = input()
    r, c = 0, 0
    for m in move:
        r += d[m][0]
        c += d[m][1]
    k_nr, k_nc = k_rc[0]+r, k_rc[1]+c
    if 0 <= k_nr < 8 and 0 <= k_nc < 8:
        if [k_nr, k_nc] == s_rc:
            s_nr, s_nc = s_rc[0]+r, s_rc[1]+c
            if 0 <= s_nr < 8 and 0 <= s_nc < 8:
                k_rc[0], k_rc[1] = k_nr, k_nc
                s_rc[0], s_rc[1] = s_nr, s_nc
        else:
            k_rc[0], k_rc[1] = k_nr, k_nc

print(get_pos(k_rc))
print(get_pos(s_rc))
