def find_num(phone, number):
    for i in range(4):
        for j in range(3):
            if phone[i][j] == number:
                return [i, j]


def solution(numbers, hand):
    answer = ''

    phone = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             ['*', 0, '#']]

    now_hands = [[3, 0], [3, 2]]

    for number in numbers:
        now_loc = find_num(phone, number)
        if now_loc[1] == 0:
            now_hands[0] = now_loc
            answer += 'L'
        elif now_loc[1] == 2:
            now_hands[1] = now_loc
            answer += 'R'
        else:
            distance = []
            for h in now_hands:
                distance.append(abs(now_loc[0] - h[0]) + abs(now_loc[1] - h[1]))
            if distance[0] < distance[1] or (distance[0] == distance[1] and hand == 'left'):
                now_hands[0] = now_loc
                answer += 'L'
            elif distance[0] > distance[1] or (distance[0] == distance[1] and hand == 'right'):
                now_hands[1] = now_loc
                answer += 'R'

    return answer
