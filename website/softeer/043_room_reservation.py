import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rooms = dict()
for _ in range(n):
    rooms[input().rstrip()] = [True] * 18
rooms = dict(sorted(rooms.items()))

for _ in range(m):
    name, r, s = input().split()
    r, s = int(r), int(s)
    for i in range(r, s):
        rooms[name][i] = False


def find_available(data):
    data = data[9:]
    index_list = []
    sub = []
    for i in range(len(data)):
        if data[i] == True:
            sub.append(i+9)
        else:
            if len(sub) >= 1:
                index_list.append(sub)
                sub = []
    if len(sub) >= 1:
        index_list.append(sub)
    return index_list


for i, name in enumerate(rooms.keys()):
    print(f'Room {name}:')
    index_list = find_available(rooms[name])
    if len(index_list) == 0:
        print('Not available')
    else:
        print(f'{len(index_list)} available')
        for idx in index_list:
            first = idx[0]
            last = idx[len(idx)-1]

            if len(str(first)) == 1:
                first = '0'+str(first)

            if last != 18:
                last = str(last+1)
            else:
                last = str(last)

            print(f'{first}-{last}')

    if i < n-1:
        print('-----')
