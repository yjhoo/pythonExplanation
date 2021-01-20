# 동전교환
# 다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.
# ▣ 입력설명 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종 류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다. 각 동전의 종류는 100원을 넘지 않는다.
# ▣ 출력설명 첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
# ▣ 입력예제 1                                   3 1 2 5 15
# ▣ 출력예제 1 3
# 설명 : 5 5 5 동전 3개로 거슬러 줄 수 있다.

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_exchange(v, m, c):
    global cnt
    # c >= cnt면 진행안함
    if c < cnt:
        # 최종에 도달했을때 m==0이면 cnt = c
        if v == N:
            if m == 0:
                cnt = c
        else:
            # l[v] 값을 추가하면 그 갯수만큼 c 추가 및 m 감소하고 v + 1해서 다음으로 넘어감
            for i in range(0, m//l[v] + 1):
                if c + i > cnt:
                    break
                f_exchange(v+1, m - (l[v] * i), c + i)

N = int(input())
l = list(map(int, input().split()))
M = int(input())
li = [0] * N
l.sort(reverse=True)
cnt = M
f_exchange(0, M, 0)
print(cnt)
