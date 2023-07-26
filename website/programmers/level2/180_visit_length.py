def solution(dirs):
    answer = set()
    x, y = 0, 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dir_dict = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

    for d in dirs:
        nx, ny = x + dx[dir_dict[d]], y + dy[dir_dict[d]]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add(tuple(sorted([(x, y), (nx, ny)])))
            x, y = nx, ny

    return len(answer)
