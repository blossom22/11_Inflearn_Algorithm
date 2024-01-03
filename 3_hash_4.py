# 해시 문제4_팰린드롬 확인
from collections import Counter
def solution(s):
    answer = False
    even, odd = 0,0
    n = Counter(s)
    val = n.values()
    for i in val:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if odd==1 or odd==0:    # 빈도수가 홀수인 경우가 1이거나, 아예 없는 경우만 팰린드롬가능 
        answer=True
    return answer     

print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))


# 위의 풀이를 좀 더 간결하게 만들었다. 
from collections import Counter
def solution(s):
    answer = False
    n = Counter(s)
    odd = 0     # 빈도수가 홀수인 경우는 1번만 있거나 아예 없어야 팰린드롬이 만들어질 수 있다. 
    for key in n:
        if n[key]%2==1:
            odd+=1
    if odd==1 or odd==0:
        answer = True
    return answer
    # 위의 3줄을 answer변수를 쓰지않고  "return odd<=1"  로 간단히 표현가능하다.
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))