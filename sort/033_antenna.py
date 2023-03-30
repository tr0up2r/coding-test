n = int(input())
data = list(map(int, input().split()))
data.sort()

# 정확히 중간값에 해당하는 위치에 안테나를 설치해야 거리 최소
# 왼쪽에 있는 집이 오른쪽에 있는 집보다 많아지기 전이 최소
print(data[(n-1) // 2])
