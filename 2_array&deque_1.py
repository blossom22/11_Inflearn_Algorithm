# 배열 & 연결리스트 & 데크
# 문제1_최솟값의 위치
# 그냥 배열에서 순차탐색을 하면서 최소값을 찾으면 된다. 시간복잡도는 O(n)
def sol(nums):
    answer = 0
    minN = 1000000
    n = len(nums)
    for i in range(n):
        if nums[i]<minN:
            minN = nums[i]
            answer = i
    return answer

print(sol([7, 10, 5, 3, 2, 15, 19]))
print(sol([-12, 12, 30, -15, -5, 3, 9, -11, 14]))
print(sol([17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]))
print(sol([7, 5, 12, -9, -12, 22, -30, -35, -21]))


# 아래처럼 그냥 index함수를 쓰는 방법도 있다. 
def sol(nums):
    return nums.index(min(nums))
