## 재귀함수&DFS_문제4: 픽셀수 구하기
# 앞서 3번에서 풀었던 것과 유사하다. 
# 다른점은 DFS가 호출되는 횟수를 세면 된다. 그것이 곧 한 영역의 픽셀 수 이다.  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(x,y,board):
    global cnt      # 위에서 쓴 cnt = 0 (전역변수)를 쓸 것이라고 명시해야한다.
    board[x][y]=0
    cnt+=1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:      # 격자안이면서, 인접한 4방향에 1인위치(검은색칸)가 있다면 그곳으로 재귀함수 호출
            DFS(nx, ny, board)

def solution(board):
    global cnt      # 전역변수 선언 해줘야한다!
    answer = []
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                cnt = 0     # 새로운 다음 검은영역을 발견했을때, 0으로 초기화하는 것
                DFS(i,j,board)
                answer.append(cnt)
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

