def solution(lottos, win_nums):
    correct = 0

    prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for num in win_nums:
        if num in lottos:
            correct += 1

    return [prize[correct + lottos.count(0)], prize[correct]]
