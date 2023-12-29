## 스택&큐_문제1: 올바른 괄호
# 코테에서 괄호( (), {}, [] )들이 문제로 나온다면 십중팔구 스택을 이용하는 문제이다.
# 또는 음수와양수, 이웃한 두문자 지우기 등등 한쌍, 한짝으로 구성된 문제들은 전부 스택을 사용한다

# 한 스택에 계속 여는 괄호가 들어가서 쌓이다가 닫는 괄호를 처음 만났을때 상황을 보자.
# 이때, 스택에서 가장 last in 된 괄호가 처음으로 만난 닫는 괄호의 짝이지.
# 짝을 만나면, last in 된 여는 괄호를 pop()하면 된다. 
def solution(s):
    answer = "YES"
    stack = []
    for i in s:
        # 닫는 괄호인데, stack이 비었으면 NO반환, 안 비었으면 pop해
        if i==')':
            if len(stack)==0:
                return 'NO'
            stack.pop()
        # 여는 괄호이면, stack에 append
        else:
            stack.append(i)
    # 선형탐색 전부 했는데 최종적으로 만들어진 stack에 여는괄호가 더 많은 경우 NO
    if len(stack)>0:
        return 'NO'
    return answer

print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))

