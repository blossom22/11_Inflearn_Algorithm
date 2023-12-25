# Sorting문제2_두 수의 차
# 문제: 정확성과 효율성테스트를 모두 한다.
# 정확성 / 효율성 모두를 해결해야한다. 정확성은 입력의 크기를 작게해서 답이 나오나보고, 효율성은 입력의 크기를 크게해서 시간초과여부를 보는 것이다.
# 이렇게 정확성, 효율성 모두 보는 문제가 코테에서 나온다. 
# 효율성목적으로하면, O(n), O(nlogn)에 준하는 알고리즘을 사용해야한다.
# 그러나 이런게 생각나지 안나면, O(n**2)로 풀어서 정확성이라도 맞춰야지...
# 문제조건: nums[i]는 1이상 1000이하이다. 

# O(n**2)로 풀어보았다. (이중for문)
def solution(nums):
    nums.sort()
    answer = []
    n = len(nums)
    a = 1000     # a의 초기값을 큰 수로 설정한다. 
    # 아래는 가장 작은 두 수의 차를 구하는 과정
    for i in range(n):
        for j in range(i+1,n):
            if nums[j]-nums[i]<a:
                a = nums[j]-nums[i]
    # 위에서 구한 가장 작은 두 수의 차(a)에 해당되는 쌍을 찾는 과정
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[j]-nums[i]==a:
                answer.append([nums[i],nums[j]])
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))


# 아래처럼 풀 수도 있다. (위와 큰 차이는 없다. O(n**2)풀이)
def solution(nums):
    answer = []
    n = len(nums)
    a = 1000
    for i in range(n):
        for j in range(i+1,n):
            diff = abs(nums[i]-nums[j])     # 두 수의 차니까 절대값(음수 X)
            if diff<a:
                a = diff
    for i in range(n):
        for j in range(i+1,n):
            diff = abs(nums[i]-nums[j])
            if diff == a:
                answer.append(sorted([nums[i], nums[j]]))
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
