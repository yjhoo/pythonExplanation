# 합이 같은 부분집합(DFS : 아마존 인터뷰)
# N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요. 둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다. 예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.
# ▣ 입력설명 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다. 두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.
# ▣ 출력설명 첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.
# ▣ 입력예제 1  6 1 3 5 6 7 10
# ▣ 출력예제 1 YES

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

# 체크된 수 vs 체크안된 수의 합으로 하여 합이 같은 경우가 있으면 프로그램 종료
def f_check(v):
    if v == N:
        tmp1 = 0
        tmp2 = 0
        for i in range(0, N):
            if a[i] == 1:
                tmp1 += l[i]
            else:
                tmp2 += l[i]
        if tmp1 == tmp2:
            print("YES")
            sys.exit()
    else:
        # 체크하고 진행할때, 안하고 진행할때를 한번씩 수행
        a[v] = 1
        f_check(v+1)
        a[v] = 0
        f_check(v+1)

N = int(input())
l = list(map(int, input().split()))
a = [0] * (N+1)
f_check(0)
print("NO")
