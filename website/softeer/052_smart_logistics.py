import sys
input = sys.stdin.readline

# n: 라인의 길이, k: 부품을 집을 수 있는 거리
n, k = map(int, input().split())

# 문자열 리스트로 만들기
data = list(input().rstrip())

result = 0
for i in range(n):
    if data[i] == 'P':
        now_k = k

        for j in range(-k+i, k+i+1):
            if j < 0 or j > n-1:
                continue
            elif data[j] == 'H':
                data[j] = None
                result += 1
                break

print(result)
