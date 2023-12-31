### BFS_문제2: 검정색 영역구하기 
'''
앞서 이 문제를 DFS로 해결했었다. 이번에는 BFS(레벨탐색)로 풀어보겠다.
> 이중 for문 선형탐색하면서 1(검은영역)을 발견하면 해당 좌표를 Q에 집어넣는다.
> 그 영역의 값은 0으로 업데이트시켜서 검색한 영역은 못가게 막는다.
> 그 영역의 자식(인접한 지역)들에서 1인 영역을 찾아서 Q에 집어넣고, 값은 0으로 바꿔

'''
dx=[-1,0,1,0]
dy=[0,1,0,-1]
from collections import deque
def BFS(x,y,board):
    Q = deque()
    Q.append([x,y])
    board[x][y] = 0     # 검은영역 찾으면 그 지역은 0으로 바꾼다. 재검색 방지
    L = 0               # 이번 코드에서 Level을 직접 쓰는일은 없지만 BFS공부하는겸 선언하자. 어려운 문제풀때 레벨탐색 쓰는일 많다
    while Q:
        n = len(Q)
        for i in range(n):
            x,y = Q.popleft()   # 찾은 검은 영역의 4방향을 탐색해서 1인 지역을 찾는ㄷ.
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:
                    Q.append([nx,ny])   # 새롭게 찾은 검은 영역을 Q에 추가하고, 찾은 영역의 값은 0 으로 바꿔라.
                    board[nx][ny] = 0
        L+=1

def solution(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                answer += 1
                BFS(i,j,board)
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

