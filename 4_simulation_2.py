# 시뮬레이션 문제2_청소로봇(ver1)
# 문제조건: 격자판 밖으로 나가는 명령은 입력되지 않는다. 
# dx, dy정할때 헷갈리지 않게 12시, 3시, 6시, 9시순으로 적자~ 
def solution(moves):
    x,y = 0,0   # x=y=0해도 됨
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in moves:
        if i=="U":
            x+=dx[0]
            y+=dy[0]
        elif i=="R":
            x+=dx[1]
            y+=dy[1]
        elif i=="D":
            x+=dx[2]
            y+=dy[2]
        elif i=="L":
            x+=dx[3]
            y+=dy[3]
    return [x,y]
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))

# 위의 코드는 if문을 하나하나 입력해서 해결하였다.
# if문들을 조금 더 간결하게 만들어보자. (위의 풀이 리팩토링)
def solution(moves):
    x,y = 0,0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ["U", "R", "D", "L"]  # 인덱스번호 0,1,2,3에 U,R,D,L 매칭시켜둬
    for i in moves:
        for k in range(4):
            if i==dir[k]:   # k는 0~3돌면서 i가 dir[k]와 같은 것일때, 위치 x,y값을 업데이트한다.  
                x+=dx[k]
                y+=dy[k]
    return [x,y]
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))