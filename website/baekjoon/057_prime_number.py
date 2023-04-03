import sys
import math
input = sys.stdin.readline

# m 이상 n 이하의 소수 구하기
m, n = map(int, input().split())
array = [True] * 1000001  # 처음엔 다 소수
array[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if array[i]:  # array[i]가 소수면 그 배수 다 소수 아님
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1


for i in range(m, n+1):
    if array[i]:
        print(i)
