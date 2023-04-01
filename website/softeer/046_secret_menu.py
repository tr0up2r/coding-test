import sys
input = sys.stdin.readline

# m: 비밀 메뉴 조작법 정수 개수, n: 사용자의 버튼 조작 정수 개수, k: 버튼 수
m, n, k = map(int, input().split())

pattern = input().rstrip().replace(' ', '')
user = input().rstrip().replace(' ', '')

if pattern in user:
    print('secret')
else:
    print('normal')
