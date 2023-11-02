arr = [['']*15 for _ in range(5)]
for i in range(5):
    for j, v in enumerate(list(input())):
        arr[i][j] = v
for i in range(15):
    print(''.join(list(zip(*arr))[i]), end='')