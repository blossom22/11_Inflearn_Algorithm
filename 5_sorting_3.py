# Sorting문제3_두 수의 합
### O(nlogn)으로 해결하였다. 
def solution(nums, target):
    answer = [0]*2
    nums.sort()
    n = len(nums)
    for i in range(n):
        if target-nums[i] in nums and target-nums[i]!=nums[i]:
            answer = sorted([nums[i], target-nums[i]])
    return answer
    
print(solution([3, 7, 2, 12, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))


### Two-pointer 알고리즘 
# 일단 nums를 정렬하고, left, right 값(nums의 인덱스)을 0,n-1로 설정해서 진행한다. 
# nums[left]+nums[right]이 크다면 right을 줄이고, 작다면, left를 키워야지
def solution(nums, target):
    answer = [0]*2
    nums.sort()
    left,right = 0,len(nums)-1
    while left<right:
        hap = nums[left] + nums[right]
        if hap>target:
            right -=1
        elif hap<target:
            left+=1
        else:
            answer = [nums[left], nums[right]]
            return answer
    return answer

print(solution([3, 7, 2, 12, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))