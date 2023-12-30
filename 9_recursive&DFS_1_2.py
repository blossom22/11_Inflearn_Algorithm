'''
<이진트리 깊이우선탐색(DFS) 예시>
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)
DFS(1)

앞서 9_recursive&DFS_1.py에서 말했듯이, 재귀함수는 stack을 쓴다.
1. DFS(1)호출시, 1을 출력후, DFS(1)-5번라인 정보가 stack에 저장되고(sleep), DFS(2)가 호출(stack에 저장)
2. DFS(2)호출시, 2를 출력후, DFS(2)-5번라인 정보가 stack에 저장되고(sleep), DFS(4)가 호출(stack에 저장)
3. DFS(4)호출시, 4를 출력후, DFS(4)-5번라인 정보가 stack에 저장되고(sleep), DFS(8)호출(stack에 저장)
4. DFS(8)호출시, if문에 의해 return(자기할일다했음)하고, stack에서 pop된다. 
5. 그래서 다시 stack의 최상단인 DFS(4)-5번라인 stack frame으로 back한 것이다.
6. 그럼 DFS(4)의 6번라인을 실행하면, DFS(9)호출 > DFS(9)도 if문에 의해 return(stack에서 pop됨)
7. DFS(4)-6번라인 stack frame으로 back한다 > DFS(4)도 다 출력한 것이어서 stack에서 pop된다.
8. 이제는 stack에서 최상단이 DFS(2)-5번라인 stack frame으로 되었다.
9. DFS(2)-6번라인을 실행하면, DFS(5)호출 > print문에 의해 5출력하고, DFS(5)-5번라인 정보가 stack에 저장되고, DFS(10)호출
10. DFS(10)은 return해서 pop되고, 다시 DFS(5)-5번라인으로 back된다
11. DFS(11)이 호출되지만, DFS(11)은 return>pop된다. DFS(5)-6번라인으로 복귀했지만 더이상 출력할 것 없어 이것도 pop된다.
12. DFS(2)-6번라인으로 back된다. 이것도 더이상 실행할 것이 없어, pop된다.
13. DFS(1)-5번라인으로 back된다. 여기서 6번라인을 실행하면, DFS(3)호출
14. ....같은방식으로 깊이우선탐색을 진행하는 것이다!

위의 과정이 스택을 직접그리지 않고도 머릿속에서 그려져야한다. 
'''