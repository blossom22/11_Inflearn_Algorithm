## 스택&큐_문제3: 연속된 문자 지우기
# 이웃한 수를 제거한다 = Stack을 쓰자
def solution(s):
    answer = ""
    stack = []
    for i in s:
        # stack이 비어있지 않고, stack의 가장 last in이 i와 같은 경우 pop해
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    answer = ''.join(stack)
    return answer

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))

