for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        n, s = input().split()
        arr.append((n, int(s)))
    arr.sort(key=lambda x: -x[1])
    print(arr[0][0])
