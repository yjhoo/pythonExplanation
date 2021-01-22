# 조합 구하기
# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중  M개를 뽑는 방법의 수를 출력하는 프로그 램을 작성하세요.
# ▣ 입력설명 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# ▣ 출력설명 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.
# ▣ 입력예제 1                                   4 2
# ▣ 출력예제 1 1 2 1 3 1 4 2 3 2 4 3 4 6

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_check(v, m):
    global cnt
    if v == M:
        for i in l:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        # v < M 일때 수행하고 i 값이 m 보다 클때 그 값을 m으로 하고 다음으로 넘어 갈 수 있도록 f_check 불러옴
        # 자신의 값보다 작은 값은 이미 나온 값이기 때문에 나보다 큰 값일 때만 다음으로 진행
        if v < M:
            for i in range(1+v, N+1):
                if b[i] == 0:
                    if i > m:
                        m = i
                        b[i] = 1
                        l.append(i)
                        f_check(v + 1, m)
                        b[i] = 0
                        l.remove(i)

N, M = map(int,input().split())

b = [0] * (N + 1)
l = []
cnt = 0
f_check(0, 0)
print(cnt)
