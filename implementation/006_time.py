# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중, 3이 하나라도 포함되는 모든 경우의 수 출력
# 완전 탐색

hour = int(input())
count = 0

for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
