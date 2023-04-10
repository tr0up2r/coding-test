data = []
for _ in range(9):
    data.append(int(input()))
dwarf_comb = []


def make_comb(idx, now_list):
    if len(now_list) == 7:
        dwarf_comb.append(now_list[:])
    for i in range(idx, len(data)):
        make_comb(i+1, now_list+[data[i]])


make_comb(0, [])
for comb in dwarf_comb:
    if sum(comb) == 100:
        comb.sort()
        for dwarf in comb:
            print(dwarf)
        break
