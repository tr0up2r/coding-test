n = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)
m = int(input())

for _ in range(m):
    g, s = map(int, input().split())

    if g == 1:  # 남자 - 배수들 바꿈
        for i in range(s, n+1, s):
            switch[i] = 1 - switch[i]
    else:  # 여자 - 대칭 같을 때까지 바꿈
        switch[s] = 1 - switch[s]
        l, r = s-1, s+1
        while 0 < l <= n and 0 < r <= n:
            if switch[l] == switch[r]:
                switch[l], switch[r] = 1 - switch[l], 1 - switch[r]
                l -= 1
                r += 1
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
