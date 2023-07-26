def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        new = ''
        for x in st:
            if x in skill:
                new += x

        if new == skill[:len(new)]:
            answer += 1

    return answer
