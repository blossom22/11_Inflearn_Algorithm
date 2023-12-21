# 해시 문제5_팰린드롬 길이
# 문제조건: 꼭 주어진 문자를 전부 써서 팰린드롬을 만들지 않아도 된다. 
from collections import Counter
def solution(s):
    even, odd = 0,[]
    n = Counter(s)
    val = n.values()
    for i in val:
        if i%2==0:
            even+=i
        else:
            odd.append(i)
    # 팰린드롬을 만들려면, 빈도수가 짝수인 경우는 전부 answer에 더하고, 
    # 홀수인 경우, 한 홀수만 그대로 더하고, 나머지는 1씩 빼서 짝수로 만들어서 더해야한다.
    if len(odd)>0:
        answer = even + sum(odd)-(len(odd)-1)
    else:
        answer = even
    return answer   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))


# 위의 코드를 좀 더 간결하게 표현해보았다. 
# 그냥 초기의 s(즉, 문자열전부)를 이용하면 굳이 짝수인경우의 빈도수들을 조건문걸면서 더할 필요 없겠지. 
from collections import Counter
def solution(s):
    n = Counter(s)
    odd = 0
    for key in n:
        if n[key]%2==1:
            odd+=1
    # 홀수빈도수를 가지는 문자가 존재할 때만, 아래처럼 len(s)-odd+1 이고, 전부 짝수빈도수인 경우, 그냥 len(s)가 답이겠지. 
    return len(s)-odd+1 if odd>0 else len(s)  

print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))