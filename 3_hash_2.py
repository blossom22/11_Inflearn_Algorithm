# 해시
# 문제2_빈도수(ver2): 딕셔너리(해시)를 사용한 풀이이다. 
# 앞서 문제1_빈도수(ver1)는 Direct-address table로 풀 수 있었지만, 이 문제는 원소의 크기가 10억까지 커져서 이 방법은 불가능하다.
# 따라서 딕셔너리(해시테이블)를 사용해야한다. 
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
print(solution([2235253, 5525612, 142561567, 123456789, 2235253, 560, 123456789, 142561567]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))


# 수나 문자의 빈도수 카운팅할때, defaultdict를 사용하면 편하다. 
from collections import defaultdict
def solution(nums):
    answer = -1
    n = defaultdict(int)    # defaultdict를 사용하며, value값은 int라고 지정
    # defaultdict는 따로 엔트리 안넣었어도, 찾는 key값의 디폴트를 0으로 지정한다. 
    for i in nums:
        n[i] += 1
    for key in n:
        if n[key]==1:
            answer = max(answer, key)
    return answer
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253, 560, 123456789, 142561567]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))


# 또는 Counter를 쓰는 방법도 있다.
from collections import Counter
def solution(nums):
    answer = -1
    n = Counter(nums)   # nums의 빈도수를 count해서 딕셔너리 꼴로 만들어줌
    for key in n:
        if n[key]==1:
            answer = max(answer, key)
    return answer
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253, 560, 123456789, 142561567]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))

