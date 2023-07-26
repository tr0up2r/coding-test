def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    while A:
        if A[0] < B[0]:
            answer += 1
            A.pop(0)
            B.pop(0)
        else:
            A.pop(0)

    return answer
