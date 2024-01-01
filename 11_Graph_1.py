'''
그래프는 연결되어 있는 원소간의 관계를 표현하는 것이다. 
이거를 코드로 짤 수 있어야한다. 
edge는 vertext간의 연결된 선을 의미한다.  
그래프는 2차원배열 or 인접리스트로 표현가능하다. 
'''

### Graph_문제1: 컴퓨터 개수
## 인접행렬로 해결해보았다. 
cnt = 0
def DFS(v, graph, ch, n):
    global cnt
    ch[v] = 1   # 이미 갔던 지역은 또 안가기 위해 count한다.
    cnt += 1    # DFS를 호출한 횟수가 곧 연결된 점의 개수여서 cnt+=1
    # v노드에 연결된 점을 찾는 과정
    for i in range(1,n+1):
        # v에 연결된 i컴퓨터가 있는지 + i컴퓨터가 방문을 안 한 것인지 확인
        if graph[v][i]==1 and ch[i]==0:
            DFS(i,graph, ch, n)

def solution(n, edges):
    global cnt
    ch = [0]*(n+1)
    graph = [[0]*(n+1) for _ in range(n+1)]
    for [a,b] in edges:
        graph[a][b] = 1
        graph[b][a] = 1
    cnt = 0
    # 1번 정점에서 출발하며, graph, ch, n 모두 solution내의 지역변수이므로, 매개변수칸에 넣어서 DFS에 넘겨줘야한다
    DFS(1, graph, ch, n)
    # 전체 개수에서 cnt(1컴퓨터에 연결된 것들 개수)를 빼면 답이다. 
    return n-cnt    
                    
print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))


## 인접리스트로 해결해보았다. 
cnt = 0
def DFS(v, graph, ch, n):
    global cnt
    ch[v] = 1  
    cnt += 1 
    # 인접리스트 탐색시, nv는 당연히 v와 연결된 노드 번호이다. 
    # 그래서 v와의 관계를 따로 확인할 필요없다. 당연히, v랑 연결된 노드이기때문에 방문여부만 확인하면된다(아래 if문)
    for nv in graph[v]:
        # 방문하지 않았던 노드에 한해서 이동시켜라
        if ch[nv]==0:
            DFS(nv, graph, ch, n)

def solution(n, edges):
    global cnt
    ch = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for [a,b] in edges:
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    DFS(1, graph, ch, n)
    return n-cnt    
                    
print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))