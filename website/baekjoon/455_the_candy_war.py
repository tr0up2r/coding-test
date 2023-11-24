for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        if arr[i]%2:
            arr[i] += 1
    while len(set(arr)) != 1:
        adder = []
        for i in range(n):
            adder.append(arr[i]//2)
        for i in range(n):
            arr[i] -= adder[i]
            arr[(i+1)%n] += adder[i]
        for i in range(n):
            if arr[i] % 2:
                arr[i] += 1
        answer += 1
    print(answer)
