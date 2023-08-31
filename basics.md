# 1. Stack 활용  

### 프로그래머스 Lv. 2 - *괄호 회전하기*

```python
def is_correct(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):
        if s[i] in brackets.values():
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                if stack[-1] != brackets[s[i]]:
                    return False
                else:
                    stack.pop()
    if stack:
        return False
    return True
```

stack 구조 + dict로 풀 수 있음.  
replace() 함수를 이용해서도 풀 수 있을 듯.  
</br>

# 2. Counter 활용  

### 프로그래머스 Lv. 2 - *튜플*

```python
from collections import Counter

def solution(s):
    answer = sorted(list(map(int, s.replace('{', '').replace('}', '').split(','))))
    
    return list(map(lambda x:x[0], sorted(Counter(answer).items(), key=lambda x: x[1], reverse=True)))
```

Counter는 dictionary에서 제공하는 function 사용 가능. (ex. items())  
dict의 value를 기준으로 정렬하기 위해서는 sorted, 혹은 sort 함수의 key에 lambda식 적용.  

### 프로그래머스 Lv. 2 - *뉴스 클러스터링*

```python
from collections import Counter


def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    if not str1 and not str2:
        return 1 * 65536
    
    c1, c2 = Counter(str1), Counter(str2)
    
    return int(sum((c1 & c2).values()) / sum((c1 | c2).values()) * 65536)
```

Counter 객체에 &, |과 같은 집합 연산자 사용 가능.  
& 는 value가 작은 것을 기준으로, |는 value가 큰 것을 기준으로 하나씩 가져옴.  
</br>

# 3. 배열 초기화  

```python
arr1 = [[0] * n for _ in range(n)]  # (O)
arr2 = [[0] * n] * n  # (X)
```

배열 초기화 시, arr1을 선언한 방법으로 해야 함.  
arr2를 선언한 방법으로 하면 n개의 [0] * n은 모두 같은 객체로 인식하여, 값 변경 시 틀림.  
</br>

# 4. product  

### 프로그래머스 Lv. 2 - *모음 사전*  

```python
from itertools import product


# product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = []
    for i in range(1, len(alpha) + 1):
        answer.extend(list(map(''.join, list(product(alpha, repeat=i)))))

    return sorted(answer).index(word) + 1
```  

product의 경우, combinations, permutations와는 달리, 중복 포함 몇 개 뽑을지를 **repeat** 인자에 넘겨줘야 함.  
(그냥 product(alpha, 1))처럼 쓰면 오류 발생.)  
</br>  

# 5. Heap 활용  

### 프로그래머스 Lv. 3 - *야근 지수*  

```python
from heapq import heapify, heappush, heappop


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-1 * w for w in works]
    heapify(works)
    for _ in range(n):
        heappush(works, heappop(works) + 1)

    return sum([w ** 2 for w in works])
```  

파이썬의 **heapq** 모듈을 활용해 우선순위 큐를 구현할 수 있음.  
기본적으로 최소 힙 형태로 정렬되고, 음수를 곱하여 최대 힙으로 활용 가능.  
최댓값, 최솟값을 매우 빠르게 찾을 수 있음.  

**heapify(l)**: 매개변수로 주어진 리스트 l을 즉시 heap으로 변환. (*O(N)*)  
**heappush(heap, item)**: item을 heap에 추가.  
**heappop(heap)**: heap의 최솟값을 return. (빈 heap일 경우 IndexError)  
</br>  

# 6. lambda 활용  

### 프로그래머스 Lv. 2 - *방금그곡*  

```python
# ... 중략 ...
answer.append((idx, info_list[2], playtime))

answer.sort(key=lambda x: (x[2], -x[0]))
return answer[-1][1]
```  

iterable 자료형을 원소로 가지는 list를 sort할 때, key에 lambda 함수를 넣어 특정 원소를 기준으로 정렬할 수 있음.  
위 문제에서는 playtime이 가장 긴 원소를 반환하되, 가장 긴 playtime을 가지는 원소가 여러 개일 경우, idx가 제일 작은 것을 반환해야 했음.  
이럴 경우 key를 위와 같이 넣어주면, playtime 기준 오름차순 정렬 후, playtime이 같은 원소는 idx 기준 내림차순 정렬할 수 있음.  

### 백준 실버 3 - *패션왕 신해빈 (9375번)*  

```python
from functools import reduce

# ... 중략 ...

counts = list(map(lambda x: x+1, d.values()))
print(reduce(lambda x, y: x * y, counts)-1)
```  

lambda와 **reduce**를 결합해, list의 각 원소들에 특정 연산을 적용한 뒤, 그것을 누적한 하나의 결과값을 낼 수 있음.  
위 문제에선 list의 모든 원소들의 곱을 구하는 데 사용해봤음.  
</br>

# 7. Dictionary (dict) 활용  

### 백준 실버 4 - *나는야 포켓몬 마스터 이다솜 (1620번)*  

```python
import sys


n, m = map(int, input().split())
names = dict()

for i in range(1, n+1):
    names[sys.stdin.readline().rstrip()] = i

nums = dict(map(reversed, names.items()))

for _ in range(m):
    now = sys.stdin.readline().rstrip()
    if now.isalpha():
        print(names[now])
    else:
        print(nums[int(now)])
```  

map을 이용해 dict의 모든 원소에 **reversed**를 적용해주면 **key, value가 뒤바뀐 새 dictionary**를 생성할 수 있음.  
</br>

# 8. 분할 정복 예시  

### 프로그래머스 Lv. 2 - *쿼드압축 후 개수 세기*  

```python
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
```  
</br>

# 9. 정렬 구현  

### 9-1) *합병 정렬*  

```python
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def merge(start, end):
    mid = (start + end) // 2
    res = []
    l, r = start, mid+1

    while l <= mid and r <= end:
        if arr[l] <= arr[r]:
            res.append(arr[l])
            l += 1
        else:
            res.append(arr[r])
            r += 1

    res += arr[l:mid+1]
    res += arr[r:end+1]

    for i in range(start, end+1):
        arr[i] = res[i-start]


def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, end)


merge_sort(0, len(arr)-1)
for n in arr:
    print(n)
```  