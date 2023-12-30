'''
<재귀함수 예시>
def DFS(n):                 0번라인
    if n==0:                1번라인
        return              2번라인
    else:                   3번라인
        DFS(n-1)            4번라인
        print(n, end=' ')   5번라인
DFS(5)

<재귀함수의 실행 원리> (꼭 알아야 나중에 백트래킹 같은 것 할 수 있다!!!)
함수가 호출되면 함수의 정보가 stack에 저장된다. (stack frame)
stack frame에는 함수의 매개변수, 지역변수, 복귀주소(호출되고 돌아오는 지점)가 저장되있다. 
1. DFS(5)를 호출하면, n=5라는 정보가 stack frame에 저장되는 것.
또한 DFS(5)를 호출하면, 4번라인(복귀주소)까지 했다는 정보가 stack frame에 저장되고, DFS(4)를 호출한다.
2. 그리고 DFS(5)는 sleep상태로 들어가고, stack에 DFS(4)가 저장된다. 
3. DFS(4)도 4번라인까지 진행되었다고 stack frame에 기록되고, DFS(3)을 호출 + DFS(4)는 sleep상태로 된다
4. 이런식으로 DFS(0)까지 stack에 저장, DFS(1)~DFS(5)는 sleep상태로 stack에 저장된다.
5. DFS(0)은 2번라인에서 return하고 기능이 끝나. 기능이 끝나면, DFS(0) stack frame은 pop하고 사라져
6. 그럼 stack의 제일상단은 sleep상태인 DFS(1)이 작동한다. 복귀주소로 돌아와서 DFS(1)의 5번라인부터 실행한다.
7. 그래서 print(1, end = ' ')가 실행되고, DFS(1)은 stack에서 pop된다. 이제 DFS(2)를 실행시켜~~
8. 같은원리로 순차적으로 stack에서 상단에 있는 것을 실행하면, 1 2 3 4 5 로 출력된다.
'''

## 재귀함수&DFS_문제1: n! 구하기

def DFS(n):
    if n==1:
        return 1
    else:
        return n*DFS(n-1)

print(DFS(5))             
print(DFS(6))
print(DFS(7))
print(DFS(8))