# 1. 괄호 문제  

stack 구조 + dict로 풀 수 있음.

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

replace() 함수를 이용해서도 풀 수 있을 듯.  
</br>

# 2. Counter 활용 + value를 기준으로 정렬하기  

```python
from collections import Counter

def solution(s):
    answer = sorted(list(map(int, s.replace('{', '').replace('}', '').split(','))))
    
    return list(map(lambda x:x[0], sorted(Counter(answer).items(), key=lambda x: x[1], reverse=True)))
```

Counter는 dictionary에서 제공하는 function 사용 가능. (ex. items())  
