# 해시 문제6_두 수의 합
# 조건: nums의 길이가 20만이하이다. 즉, 시간복잡도 고려해야는 문제
# O(n**2)코드는 불가능(이중for문 X)
# O(n)으로 해결 or O(nlogn)으로 해결해야한다. 
# O(n)으로 해결해보자. 
# 배열part에서 이 문제를 풀때는 x+y=target이 되는 x,y를 찾기위해 이중for문을 돌렸지.
# 생각을 바꿔서 y = target-x로 보자. 
# x를 for문 한번으로 탐색하면서, target-x가 x의 앞쪽에 존재했었는지 탐색한다! 있으면 그게 x의 짝인 y이다. 
# 만약 target-x가 x의 앞에 존재하지 않았다면, 한 딕셔너리에 이 key가 존재했다는 의미에서 추가해준다. 
from collections import defaultdict
def solution(nums, target):
    answer = [0]*2
    n = defaultdict(int)
    for key in nums:
        if (target-key) not in n:
            n[key]+=1
        else:
            answer = sorted([key,target-key])
    return answer
                
print(solution([3, 7, 2, 12, 9, 15, 8], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))


# 위의 코드를 좀 더 간결하게하면 아래와 같다.
from collections import defaultdict
def solution(nums, target):
    answer = [0]*2
    n = defaultdict(int)
    for x in nums:
        y = target - x
        if y in n:
            return sorted([x,y])
        n[x] = 1
    return answer
print(solution([3, 7, 2, 12, 9, 15, 8], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))
