# 해시 문제3_자기분열수 - Counter를 이용하여 딕셔너리를 만들어서 해결했다. 
# nums의 길이가 3이상 50만이하이다. 즉, 매우 길어서 효율성 고려해야한다. 
# (O(n제곱) 쓰면 안됨. 그렇다고 꼭 O(n)만 쓰려고 할 필요는 없다)
# (문제에 따라서 O(nlogn)으로 풀어도 됨(sort가 O(nlogn))) 
# 보통 프로그래머스에서 설정되있는 문제풀이 제한시간은  "정답코드처리시간 * 3"  이다. 

# 또한 배열nums의 원소는 100만까지 커진다 = Direct-address table사용하지 말고, hash table사용해야한다(딕셔너리)
from collections import Counter
def solution(nums):
    answer = -1
    temp = []
    n = Counter(nums)
    for key in n:
        if n[key] == key:
            temp.append(key)
    if len(temp)>0:
        answer = min(temp)
    return answer

print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))


# answer를 초기에 매우 큰 값으로 초기설정하고 min으로 찾는 방법
from collections import Counter
def solution(nums):
    answer = 100000000  # answer를 가능한 자기분열수 중 가장 큰 값으로 초기설정하기 
    n = Counter(nums)
    for key in n:
        if n[key] == key:
            answer = min(answer, key)
    if answer == 100000000:
        return -1
    else: 
        return answer
    # 또는 위의 4줄을     return -1 if answer==100000000 else answer   로 줄여쓸 수 있음
print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))