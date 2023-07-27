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