## 그리디_문제2: 최대 사과의 개수
# 한 박스에 가장 많은 사과를 담은 박스부터 담아야한다
# sort한 후, 진행(O(nlogn))
def solution(box, limit):
    answer = 0
    box.sort(key=lambda v:-v[1])
    for x in box:
        cnt = min(limit, x[0])
        answer += cnt*x[1]
        limit -= cnt
        if limit==0:
            break
    return answer
print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))


# 아래는 O(n**2)풀이로 답은 나오지만 이렇게하면 안된다.(문제조건: box가 10만미만이므로 효율성 고려해야하는 문제이다)
def solution(box, limit):
    boxcnt = 0
    applecnt = 0
    box.sort(key=lambda v:(-v[1]))
    for i in box:
        for j in range(i[0]):
            boxcnt += 1 
            applecnt += i[1]
            if boxcnt==limit:
                return applecnt
print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

