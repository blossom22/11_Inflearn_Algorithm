# 배열 & 연결리스트 & 데크
# 문제3_연속된 1의 길이
# 이거도 그냥 선형탐색하면 된다. 시간복잡도는 O(n)이면 된다. 
def sol(nums):
    answer = 0
    cnt = 0
    for i in nums:
        if i==1:
            cnt+=1
            if cnt>answer:
                answer=cnt
        else:
            cnt=0
    return answer

print(sol([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(sol([0, 0, 1, 0, 1, 0, 0]))
print(sol([1, 1, 1, 1, 1]))
print(sol([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))

# 아래처럼도 가능하다.
def sol(nums):
    answer = 0
    cnt = 0
    for i in nums:
        if i==1:
            cnt+=1
        else:
            answer=max(answer,cnt)
            cnt = 0
    answer=max(answer,cnt)      # 이 줄이 없으면, nums마지막 줄까지 1이 연속된 경우, cnt만 늘리고 answer는 업데이트가 안되는 사태가 발생.
    return answer