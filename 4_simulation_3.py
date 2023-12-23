# 시뮬레이션 문제3_청소로봇(ver2)
# 앞서봤던 ver1문제와 다른점은  격자판 밖으로 나가는 명령도 입력될 수 있다. 이경우, 명령을 무시해야한다. 
# 로봇이 최종적으로 멈춘 위치를 반환하자. 
def solution(n, moves): 
    x,y = 0,0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ["U", "R", "D", "L"] 
    for i in moves:
        for k in range(4):
            if i==dir[k]:
                nx = x+dx[k]
                ny = y+dy[k]
                # 아래조건문의미: 만약 새롭게 갈 위치(nx,ny)가 격자판을 안 벗어나면 x,y(현재위치)로 업데이트해라. 격자판 벗어날 수 있다면 그 명령어는 무시해
                if nx>=0 and nx<n and ny>=0 and ny<n:
                    x+=dx[k]
                    y+=dy[k]
    return [x,y]    

print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))


# 이렇게도 풀이가능하다. 
def solution(n, moves): 
    x,y = 0,0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ["U", "R", "D", "L"] 
    for i in moves:
        for k in range(4):
            if i==dir[k]:
                nx = x+dx[k]
                ny = y+dy[k]
        # 격자판 벗어나면 무시하고 지나가고, 안 벗어나면, x,y를 nx,ny로 업데이트함.
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        x = nx
        y = ny 
    return [x,y]    

print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))
