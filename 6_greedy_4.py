## 그리디_문제4: 카드 점수 (참고로 이 문제는 greedy관련 문제는 아니다)
# O(n**2)으로 풀어보았다 (nums길이가 30만이하이므로 원래는 이렇게 풀면 안됨)
# k장씩 뽑는 경우의 수를 전부 계산해서 최대값을 출력하는 방식이다. 
def solution(nums, k):
    answer = 0
    n = len(nums)
    for i in range(k+1):
        hap = 0
        for j in range(i):
            hap += nums[j]
        for j in range(n-k+i,n):
            hap += nums[j]
        answer = max(hap, answer)
    return answer
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))


# 