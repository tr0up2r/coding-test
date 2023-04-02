from itertools import permutations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
input_rails = list(map(int, input().split()))
rails_info = permutations(input_rails, n)

result = 1e9
for now_rails in rails_info:
    rails = list(now_rails)
    i = 0
    bucket = 0
    work = 0
    this_all = 0

    while work != k:  # 작업의 수만큼 반복
        if bucket + rails[i] <= m:  # m: 바구니 무게
            bucket += rails[i]
            i = (i+1) % n
        else:
            this_all += bucket
            bucket = 0
            work += 1

    result = min(result, this_all)

print(result)
