## 이진탐색_문제1: (이진탐색 개념잡기)
def solution(nums, target):
    answer = 0
    if target in nums:
        answer = nums.index(target)
    else:
        answer = -1
    return answer
print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
# 그러나 위의 풀이 같은 선형탐색(리스트 전체를 하나하나 탐색)도 nums의 길이가 1억개(100,000,000)까지 가면 부담스럽다
# 더 효율적인 방법이 필요하다. 바로 이진탐색(O(logn)의 시간복잡도를 가짐)
# log(1억)은 약 27이다. 만약 선형탐색을 하면 최악의 경우 반복문을 1억번 돌아야하지만, 이진탐색을 쓰면 약 27번 반복으로 답 구할 수 있다

'''
이진탐색의 조건: 자료가 오름차순이든, 내림차순이든 정렬이 되어있어야 가능하다.
만약 오름차순이었다고 가정하자. 
left는 배열의 첫번째, right는 마지막 인덱스로 설정하고, mid는 (left+right)//2의 인덱스를 갖게 해라
> 이때 mid위치의 값이 target값보다 크면 mid인덱스 이상의 범위가 전부 필요없다. right=mid-1로 바꿔
> 만약 mid위치 값이 target보다 작으면 반대로 left = mid+1로 한다.
> 만약 mid위치 값이 target이면 break하면 되지. 
위의 과정을 while문으로 반복하면 된다 (left가 right보다 커지기전까지 반복)
이렇게 굳이 볼 필요가 없는 부분을 무시하면서 답을 찾는 것이 이진탐색이다.
'''
# 아래처럼 푸는 것이 이진탐색이다 : O(logn)
# 중요한 점은 자료가 오름차순 정렬이 되어있다는 사실. 정렬되어있어서 이진탐색이 가능하다
def solution(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if target==nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid+1
        else: 
            right = mid-1
    return -1       # left가 right보다 커졌다는 것은 결국 답을 못찾은 상황
print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
