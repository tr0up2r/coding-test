t = int(input())
for _ in range(t):
    n = list(str(bin(int(input()))))[2:]
    n.reverse()
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=' ')
