# 배열 & 연결리스트 & 데크
# 문제4_수열 회전
# 연결리스트로 풀어봤다. 

from collections import deque
def sol(nums, k):
    answer = deque(nums)
    for i in range(k):
        answer.append(answer.popleft())     # 왼쪽에서 하나 꺼낸 것을 바로 append해서 오른쪽 뒤로 추가시켜
    return list(answer)

print(sol([3, 7, 1, 5, 9, 2, 8], 3))
print(sol([2, 12, 2, 1, 3, 3, 9], 2))
print(sol([1, 2, 5, 4, 6, 7, 9], 6))
print(sol([1, 3, 6, 8, 14, 2, 1, 7], 5))

# 이 방법 외에도, nums를 slicing해서 앞의 k개를 뒤에 더하는 방법도 있다. 