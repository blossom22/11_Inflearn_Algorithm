## 재귀함수&DFS_문제2: 피보나치 수열
# 재귀함수로 간단히 구하면 된다. 
def DFS(n):
    if n==1 or n==2:
        return 1
    else:
        return DFS(n-2)+DFS(n-1)

print(DFS(5))
print(DFS(6))
print(DFS(8))
print(DFS(10))

'''
위의 과정이 어떻게 돌아가는지 직접 stack 그려서 한번 생각해보자.
어디가 sleep이고 어디가 호출되는지 직접 생각해볼 것.
> 초기에 D(5)하면, D(3)호출하고, D(5)-4번라인이 stack frame에 저장
> D(3)는 D(1)호출하고 sleep / D(1)은 1 return하고 pop > D(3)-4번라인이 stack의 최상단에 위치해서 실행되면, D(2)호출
> D(2)는 1 return하고 pop > D(3)은 결과적으로 1+1을 return하고 pop > D(5)-4번라인이 stack의 최상단
> 이제 D(4)를 호출해서~~~위의 과정을 반복
'''