from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, 0))
    visited = [False for _ in range(len(words))]
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            diff_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff_cnt += 1
                if diff_cnt == 1:
                    queue.append((words[i], cnt + 1))
                    visited[i] = True

    return answer
