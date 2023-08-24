def solution(arr):
    answer = [0, 0]

    def quad(start_r, start_c, size):
        num = arr[start_r][start_c]
        if size == 1:
            answer[num] += 1
            return

        for r in range(start_r, start_r + size):
            for c in range(start_c, start_c + size):
                if arr[r][c] != num:
                    size //= 2
                    quad(start_r, start_c, size)
                    quad(start_r, start_c + size, size)
                    quad(start_r + size, start_c, size)
                    quad(start_r + size, start_c + size, size)
                    return

        answer[num] += 1
        return

    quad(0, 0, len(arr))
    return answer
