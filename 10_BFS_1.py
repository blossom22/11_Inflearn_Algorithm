### 이진트리 레벨탐색(=너비우선탐색(=BFS))
## 이 문제가 BFS의 기본이다. 반복 연습하기!!
'''
- 출발지점에서 도착지점까지 가는 최단 경로(비용,횟수)를 구하는 알고리즘이다.
루트노드가 0level, 그 바로 아래노드들이 1level....이렇게 level로 표시한다.
0level 전부 방문했으면, 1level 전부 방문하고, 2level 전부 방문하고...이렇게 level순으로 탐색이 이뤄진다.
- 파이썬에서는 deque로 BFS를 구현한다.
'''

### BFS_문제1: 최소 점프
# 최소횟수, 최단거리 등등 이란 단어가있다면, BFS를 고려하기.
# 이 문제에서도 level값이 곧 점프한 횟수가 된다. 
# BFS를 하되, 이미 갔던 노드값은 중복되지 않게 코드를 짜보자.
from collections import deque
def BFS(home):
    Q = deque()
    Q.append(0)
    check = [0]*10001  # 1만번 인덱스까지 포함된 check배열 만들어.
    check[0] = 1
    L = 0
    while Q:
        n = len(Q)
        for i in range(n):
            x = Q.popleft()
            # L이 1이면 한번의 점프로 갈 수 있는 노드값, L이 2이면 두번의 점프로 갈 수 있는 노드값 
            if x==home:
                return L
            for nx in [x-1, x+1, x+5]:
                # 수직선의 좌표는 0이상 10000이하였다 & 한번도 방문 안한 노드만 봐야한다.
                if nx>=0 and nx <= 10000 and check[nx]==0:
                    Q.append(nx)
                    check[nx] = 1   # 한번 탐색한 노드의 값은 1로 만들어
        L += 1
        

def solution(home):
    answer = BFS(home)

    return answer

print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))