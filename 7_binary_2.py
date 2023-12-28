## 이진탐색_문제2: 트럭 찾기
# 짐의 무게보다 트럭의 무게제한이 크거나 같아야 한다.
# 즉, lower bound search를 진행해야한다. 
# 문제의 조건에서 nums는 오름차순 정렬이 되어있다고 했으므로, binary search를 바로 진행가능하다.
def solution(nums, weight):
    left = 0
    right = len(nums)
    while left<right:
        mid = (left+right)//2
        if weight > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return -1 if right==len(nums) else right

print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))                                          
print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solution([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
print(solution([20, 30, 40, 50, 60, 70], 90))
print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))


# 만약 bisect를 쓴다면 아래처럼 하면된다. 
from bisect import bisect_left
def solution(nums, weight):
    answer = bisect_left(nums, weight)
    return -1 if answer==len(nums) else answer

print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))                                          
print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solution([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
print(solution([20, 30, 40, 50, 60, 70], 90))
print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))