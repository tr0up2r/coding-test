from itertools import permutations


def solution(k, dungeons):
    answer = -1
    perms = list(permutations(dungeons, len(dungeons)))

    for perm in perms:
        now_k = k
        count = 0
        for d in perm:
            if d[0] > now_k:
                continue
            now_k -= d[1]
            count += 1
        answer = max(answer, count)

    return answer
