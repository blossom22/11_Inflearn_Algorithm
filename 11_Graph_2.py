### Graph_문제2: 동아리 개수
# 재귀함수 배울때 풀었던 블러드필 알고리즘 문제랑 유사하다. 
## 인접리스트로 해결하였다. 

cnt = 0
def DFS(v, graph, ch, n):
    ch[v] = 1
    for nv in graph[v]:
        if ch[nv]==0:
            DFS(nv, graph, ch, n)

def solution(n, edges):
    answer = 0
    ch = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for [a,b] in edges:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,n+1):  # ch배열에서 1씩증가시키면서 0인 부분에서만 탐색한다. 1인부분은 이미 탐색한 곳
        if ch[i]==0:
            answer +=1      # 탐색이 될때마다 1씩 증가시켜
            DFS(i, graph, ch, n)

    return answer 
print(solution(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))
print(solution(20, [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4], [4, 6], [6, 8], [8, 10], [11, 12], [14, 16], [16, 17], [17, 18], [19, 20]]))
print(solution(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(solution(30, [[5, 6], [6, 7]]))

