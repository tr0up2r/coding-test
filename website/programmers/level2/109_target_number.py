count = 0


def solution(numbers, target):
    global count
    ops = ['+', '-']

    def dfs(number, i):
        global count
        if i == len(numbers):
            if number == target:
                count += 1
            return
        for op in ops:
            if op == '+':
                number += numbers[i]
                dfs(number, i + 1)
                number -= numbers[i]
            else:
                number -= numbers[i]
                dfs(number, i + 1)
                number += numbers[i]

    dfs(0, 0)
    return count
