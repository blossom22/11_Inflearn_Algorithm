# 시뮬레이션 문제4_로봇의 이동
def solution(moves):
    x,y = 0,0
    dir = 1     # 로봇이 보는 방향에 대한 변수(dir=1이면, dx,dy가 3시방향보는 것)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in moves:
        if i=="G":
            # dir이 4이상이면 index error. dir이 3시, 6시, 9시 까지 커졌으면 다시 12시 방향으로 초기화되어야한다
            # (왼쪽으로 90도 회전하는경우): 참고로, -1을 4로 나눈 나머지는 3이다.(몫은 -1) 따라서, dir[3]이 된다. 
            # 그러나 위의 논리는 파이썬에서만 가능(자바, C++에서는 불가능)
            # 다른 언어에서 해결하려면, dir=(dir-1)%4 코드를 dir=(dir+3)%4로 바꿔야한다. (파이썬도 가능)
            x+=dx[dir%4]
            y+=dy[dir%4]
        elif i=="R":
            dir+=1
        elif i=="L":
            dir-=1
    return [x, y]
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))