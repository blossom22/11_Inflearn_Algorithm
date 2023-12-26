### 그리디 알고리즘: 매 순간 최선의 선택만 하는 방식이다.
# 코테에서 그리디 알고리즘으로 풀었을때 주의할 점은 반례가 있는지 확인해야한다!
# 문제에서 주어진 예시에서는 성립해도 반례가 있을 수 있다. 항상 그리디가 정답은 아니다. 
# 따라서 그리디를 풀때는 반례를 만드는 습관을 가지자!

## 그리디_문제1: 버스
# weight의 길이가 10만미만(즉, 효율성 고려해라)
# 최대 승객수 태우려면, 오름차순 정렬해서 작은 놈부터 버스에 태우면 되겠다. (O(nlogn))
def solution(weight, limit):
    answer = 0
    temp =0
    n = len(weight)
    weight.sort()
    for i in range(n):
        if temp+weight[i]<=limit:
            temp += weight[i]
            answer+=1
    return answer
print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))


# 위 코드를 좀 더 간결하게 바꿔보았다. 
def solution(weight, limit):
    answer = 0
    temp =0
    weight.sort()
    for x in weight:
        if temp+x > limit:
            break
        temp += x
        answer += 1 
    return answer
print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))

