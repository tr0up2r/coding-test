# 떡의 개수 n, 요청한 떡의 길이 m
# 둘째 줄에는 떡의 개별 높이

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
