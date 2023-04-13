def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    students = [0, 0, 0]

    for i, s in enumerate(answers):
        if s == p1[i % len(p1)]:
            students[0] += 1
        if s == p2[i % len(p2)]:
            students[1] += 1
        if s == p3[i % len(p3)]:
            students[2] += 1

    first = max(students)
    answer = []
    for i in range(len(students)):
        if students[i] == first:
            answer.append(i + 1)

    return answer
