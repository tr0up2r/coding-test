def solution(arr1, arr2):
    answer = []

    swap = []
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        swap.append(tmp)

    for r1 in arr1:
        tmp = []
        for r2 in swap:
            s = 0
            for v1, v2 in zip(r1, r2):
                s += v1 * v2
            tmp.append(s)
        answer.append(tmp)
    return answer
