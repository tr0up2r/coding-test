def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations)):
        if answer >= citations[i]:
            return answer
        if citations[i] <= i+1:
            return i+1
        answer += 1
    return answer
