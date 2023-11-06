# 배열 & 연결리스트 & 데크
# 문제5_중복 제거 
# n이 최대 20만이므로, 효율성 고려해야한다. 
# O(n) (선형탐색)으로 끝내야겠구나~ + 효율적인 자료구조를 써야겠구나~
# 내 풀이
from collections import deque
def sol(nums):
    nums = deque(nums);
    answer = deque()
    for i in range(len(nums)):
        a = nums.popleft()
        if a in answer:
            pass
        else:
            answer.appendleft(a)
    return list(answer)

print(sol([0, 1, 1, 1, 2, 2, 2, 3]))
print(sol([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(sol([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(sol([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))

print('--------------------')

# 선생풀이
# 일단 nums의 첫번째 원소는 반드시 넣고, 그 값과 다음에 넣을 nums의 값과 비교해서 다르면 넣고,
# 다르면 넣지 않는 방식으로 진행(넣을때는 appendleft쓰면 되겠다 = 배열말고, 연결리스트 써야겠다)
# 만약 배열을 쓴다면, 원소 하나 추가될때마다, 모든 원소들을 다 한칸씩 뒤로 이동해야해서 비효율적이다.
# 일단 answer를 데크로 만들고 하자. 나중에 결과나올때만, list()로 묶으면 되지.  
def sol(nums):
    answer = deque()
    answer.appendleft(nums[0])
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:    # 이미 넣은 원소랑 또 넣을 원소를 비교해서 다르면 추가시키기
            answer.appendleft(nums[i])
    return list(answer)
print(sol([0, 1, 1, 1, 2, 2, 2, 3]))
print(sol([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(sol([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(sol([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))