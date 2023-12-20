# 해시
# 문제1_빈도수(ver1): 딕셔너리(해시)를 사용한 풀이이다. 
def solution(nums):
    answer = -1
    n = len(nums)
    dat = {}
    for i in nums:
        if i in dat:
            dat[i] += 1
        else:
            dat[i] = 1
    for i in dat:
        if dat[i]==1 and answer<i:
            answer = i
    return answer

print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))


# 또다른 풀이: Direct-address table방법
# Nums의 원소의 크기가 1000이하의 자연수이다. 
# 즉, key가 1000개의 종류인 bucket을 전부 만든 Direct address table을 만들수 있다. (1000정도는 가능)
# (인덱스가 0번부터 1000번까지인 리스트를 만들겠다는 소리)
def solution(nums):
    answer = -1
    cnt = [0]*1001
    for i in nums:
        cnt[i]+=1
    for i in range(1,1001): 
        if cnt[i]==1:
            answer = max(answer, i)
    # 아니면 위의 3줄을 좀 더 효율적으로 바꿔보면 아래처럼 range를 거꾸로 돌면된다. 가장 큰 i값부터 돌게될테니까~
    # for i in range(1000,0,-1):
    #   if cnt[i] ==1:
    #       return i
    return answer

print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))

