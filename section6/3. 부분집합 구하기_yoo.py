# 부분집합 구하기(DFS)
# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.
# ▣ 입력설명 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
# ▣ 출력설명 첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다. 단 공집합은 출력하지 않습니다.
# ▣ 입력예제 1                                   3
# ▣ 출력예제 1 1 2 3 1 2 1 3 1 2 3 2 3

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

#부분집합을 구하는 함수
def f_DFS(v):
    # v 값이 N에 도달하면 출력
    if v == N + 1:
        for i in range(1, N + 1):
            if l[i] == 1:
                print(i, end=" ")
        print()
    else:
        # l[v] 값을 1로 하여 한번 자신이 있는 집합을 출력하고, 다시 0으로 수정하여 자신이 없는 집합을 표현
        l[v] = 1
        f_DFS(v + 1)
        l[v] = 0
        f_DFS(v + 1)

N = int(input())
l = [0] * (N + 1)
f_DFS(1)
