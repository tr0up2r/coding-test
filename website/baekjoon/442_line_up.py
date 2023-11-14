for t in range(1, int(input())+1):
    arr = list(map(int, input().split()))[1:]
    answer = 0
    for i in range(19):
        for j in range(i+1, 20):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                answer += 1
    print(t, answer)
