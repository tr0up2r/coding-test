import sys
input = sys.stdin.readline

# n: 학생 수, k: 구간 수
n, k = map(int, input().split())

# 성적
grade = list(map(int, input().split()))

# 성적 구간
section = []
for _ in range(k):
    section.append(list(map(int, input().split())))

for s in section:
    now_grade = grade[s[0]-1:s[1]]
    print(f'{sum(now_grade) / len(now_grade):.2f}')
