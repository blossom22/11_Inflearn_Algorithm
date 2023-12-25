# Sorting문제1_사탕 종류

# set를 이용해서 풀어봤다
def solution(nums):
    answer = 0
    n = len(nums)
    answer = min(int(n/2), len(set(nums)))
    return answer
print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))


# 아래는 문제 의도에 맞게 sort(O(nlogn))로 풀어본 결과이다
# nums의 길이가 10만까지도 가능하므로 시간복잡도 고려해야한다.
def solution(nums):
    temp = 1    # sorting된 nums의 첫 원소는 반드시 카운팅되니까~
    answer = 0
    n = len(nums)
    # nums정렬후, 중복된 것을 제외한 개수를 temp에 저장하자. 
    nums.sort() 
    for i in range(1,n):
        if nums[i]!=nums[i-1]:
            temp+=1
    answer = min(int(n/2), temp)    # 또는 int(n/2)말고 n//2해도 정수형으로 출력됨
    return answer
print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))

