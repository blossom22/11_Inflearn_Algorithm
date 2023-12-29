## 스택&큐_문제2: Backspace
# '#'문자가 백스페이스 키 기능을 한다면, 가장 마지막으로 append된 문자를 제거할테니, stack을 사용하자.

def solution(s):
    answer = ""
    stack = []
    for i in s:
        if i=='#':
            # 바로 아래 if문은 그냥 'if stack:' 해도 됨(stack이 비어있으면 False, 뭐라도 있으면 True니까)
            if len(stack)!=0:
                stack.pop()
        else:
            stack.append(i)
    answer = ''.join(stack)
    return answer

print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
