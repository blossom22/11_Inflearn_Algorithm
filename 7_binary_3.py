## 이진탐색_문제3: 고정된 숫자
# 그냥 선형탐색(O(n))해도 구할 수는 있지만, nums의 길이가 크니까, 이분탐색(O(logn))방식을 쓰자.
# 인덱스값이 nums[mid]값보다 크다면, 현재 mid위치보다 큰 곳들에서만 '고정된 숫자'가 있을 수 있다.
# 인덱스값이 nums[mid]보다 작다면, 현재 mid위치보다 작은 곳들에서만 '고정된 숫자'가 있을 수 있다.
# 위의 생각이 가능한 이유는 nums가 오름차순 정렬되어있고, nums의 원소가 유일값이기 때문이다.
def solution(nums):
    left = 0
    right = len(nums)-1
    while left<=right:      # 여기서 left=right인 경우도 체크해야한다! 주의
        mid = (left+right)//2
        if nums[mid]==mid:
            return mid
        if nums[mid]<mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  
