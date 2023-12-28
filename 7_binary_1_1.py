'''
파이썬에서는 lower bound search / upper bound search를 제공하는 라이브러리(bisect)가 있다.
from bisect import bisect_left, bisect_right   를 쓰면 된다.

bisect_left 는 lower bound search 를 한다.
bisect_right 는 upper bound search 를 한다.

binary search를 직접 코드로 구현하는게 좋지만, 이렇게 bisect로 바로 풀수도 있다.
그러나 코테에서 bisect를 못쓰게 막는경우도 있으므로, 구현방식은 잘 알아두자.
'''

### bisect_left
from bisect import bisect_left, bisect_right
def solution(nums, weight):
    # 아래처럼 하면, nums안에서 weight보다 크거나 같은 것들 중에서 가장 작은 값을 찾아준다
    answer = bisect_left(nums, weight)
    return answer
print(solution([70,80,80,80,80,90,90,90], 80))      # 이것의 결과는 80이 처음으로 나온 인덱스값 1이 answer로 출력됨


### bisect_right
def solution(nums, weight):
    # 아래처럼 하면, nums안에서 weight보다 큰 것 중에서 가장 작은 값을 찾아준다
    answer = bisect_right(nums, weight)
    return answer
# 아래의 print를 실행하면, 90보다 큰 값이 없다. 따라서 초기의 right값인 인덱스값 8 (len(nums)+1의 값)이 출력된다.
print(solution([70,80,80,80,80,90,90,90], 90))    

# 위같은 결과를 원하지 않다면 코드를 아래처럼 바꾸자.
def solution(nums, weight):
    answer = bisect_right(nums, weight)
    return -1 if answer==len(nums) else answer
print(solution([70,80,80,80,80,90,90,90], 90))  