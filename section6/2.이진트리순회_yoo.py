# 이진트리 순회(깊이우선탐색)
# 아래 그림과 같은 이진트리를 전위순회와 후위순회를 연습해보세요.
# 1
# 2 3
# 4 5 6 7
# 전위순회 출력 : 1 2 4 5 3 6 7 중위순회 출력 : 4 2 5 1 6 3 7 후위순회 출력 : 4 5 2 6 7 3 1


import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

# 전위순회
def f_DFS(v):
    if v <= 7:
        print(v, end=' ')
        f_DFS(2*v)
        f_DFS(2*v + 1)
# 중위순회
def f_DFS1(v1):
    if v1 <= 7:
        f_DFS1(2*v1)
        print(v1, end=' ')
        f_DFS1(2*v1 + 1)
# 후위순회
def f_DFS2(v2):
    if v2 <= 7:
        f_DFS2(2*v2)
        f_DFS2(2 * v2 + 1)
        print(v2, end=' ')

f_DFS(1)
print()
f_DFS1(1)
print()
f_DFS2(1)
