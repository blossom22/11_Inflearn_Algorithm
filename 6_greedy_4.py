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


### 이번에는 효율성테스트를 통과하도록 O(n)으로 풀어보겠다. 
### 여기서 쓸 알고리즘: 슬라이딩 윈도우
# > 길이 k인 윈도우를 만들어서 부분수열의 합을 구해 
# > 윈도우를 한칸밀어서 잡은 새로운 부분수열의 합을 구할때, 하나하나 반복문 돌면서 다시 구하지말고,
# 윈도우로 추가된 숫자하나를 더하고, 윈도우 밖으로 나간 숫자하나를 빼서 새로운 부분수열의 합을 계산해라.
# 이런방식으로하면, O(n)으로 부분수열의 합을 구할 수 있다

# 위의 슬라이딩윈도우를 이 문제에 적용시켜보자. 왼쪽끝과 오른쪽끝에서 카드를 가져갈때, 남는 것에 집중해서보자.
# 아래 print문 첫번째 문제보면, 왼쪽0개&오른쪽4개 가져가면 2,3,7남고, 왼쪽1개&오른쪽3개 가져가면, 3,7,1 남고...
# 마치 슬라이딩 윈도우가 지나가는 모습! nums전부 합한 것에서 슬라이딩 윈도우로 구한 부분수열의 합을 뺀 것들에서, 제일 큰 놈을 찾으면 된다.

# 투포인터처럼 left, right를 설정해서 부분수열의 처음과 끝을 지정하는 방식이다 
def solution(nums, k):
    hap = sum(nums)
    m = len(nums)-k     # 부분수열 하나의 크기
    score = 0
    # 아래의 for문은 맨초기의 부분수열의 합(score)을 구하는 것
    for i in range(m):
        score += nums[i]
    minS = score
    # left는 부분수열의 시작위치, right는 부분수열 끝위치의+1을 지정한다.(nums[right]를 새롭게 더하고, nums[left]는 빼주면 새로운 부분수열의 합을 구할 수 있다)
    left = 0
    for right in range(m,len(nums)):
        score += (nums[right] - nums[left])
        left+=1     # 구했으면 left+=1해서 다음 부분수열로 넘어가야지
        minS = min(minS, score)     # 구한 score들 중 최소값을 minS로 저장한다 
    return hap - minS               # hap에서 minS(부분수열합의 최소값)를 뺀 값이 최대점수이다. 
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))


# 이런 풀이도 가능했다 (But, 위의 방법대로 하자)
def solution(nums, k):
    n = len(nums)
    hap = sum(nums)
    sliding = sum(nums[:(n-k)])
    a = [sliding]
    for i in range(k):
        sliding = sliding - nums[i] + nums[i+(n-k)]
        a.append(sliding)
    answer = hap - min(a)
    return answer
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))