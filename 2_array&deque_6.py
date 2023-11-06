# 배열 & 연결리스트 & 데크
# 문제6 _두 수의 합
def solution(nums, target):
    answer = [0] * 2
    nums.sort()
    i,j = 0,1
    while True:
        a = nums[i]
        b = nums[j]
        if a+b == target:
            answer[0]=a
            answer[1]=b
            return answer
        elif a+b < target:
            j+=1
        else:
            i+=1
            j=i+1
        if i==len(nums)-1:
            return [0,0]

print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))

# 선생풀이
# 이문제는 hash섹션에서 또 다룰 것이다(이때는 입력의 크기가 커져)(O(n))
# 또한 sort섹션에서 또 다룰 것이다(이때는 O(nlogn))
# 여기선 이중 for문(O(n**2))으로 풀자. (차피 입력의 최대가 10만보다 작아서 효율성고려X)
def solution(nums, target):
    answer = [0] * 2
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return sorted([nums[i], nums[j]])
    return answer
print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))