import sys
from itertools import combinations
input = sys.stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u')

# l: 암호 길이, c: 알파벳 수
l, c = map(int, input().split())
array = input().split()
array.sort()

for password in list(combinations(array, l)):
    vowel_count = 0
    for vowel in vowels:
        if vowel in password:
            vowel_count += 1
    # 최소 한 개의 모음과 최소 2개의 자음이 있는 경우 출력
    if (vowel_count >= 1) and (vowel_count <= l-2):
        print(''.join(password))
