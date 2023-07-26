def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2:
            bin_n = bin(n)[2:][::-1]
            for i in range(len(bin_n) + 1):
                if i == len(bin_n) or bin_n[i] == '0':
                    answer.append(n + 2 ** i - (2 ** i) // 2)
                    break
        else:
            answer.append(n + 1)

    return answer
