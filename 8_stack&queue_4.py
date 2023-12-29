## 스택&큐_문제4: 샌드위치
# 짝 의 개념이 들어가 = stack으로 풀자
def solution(nums):
    answer = 0
    stack = []
    for i in nums:
        # stack에 최소한 2개이상의 자료가 있어야하고, stack[-1]=2, stack[-2]=1이어야 샌드위치 만들지
        if len(stack)>1 and stack[-2]==i and stack[-1]==2:
            answer+=1
            stack.pop()
            stack.pop()
        else:
            stack.append(i)
    return answer
    
print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
