# 동전 분배하기(DFS)
# N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다. 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요. 단 세 사람의 총액은 서로 달라야 합니다.
# ▣ 입력설명 첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다. 그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.
# ▣ 출력설명 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.
# ▣ 입력예제 1                                   7 8 9 11 12 23 15 17
# ▣ 출력예제 1 5
# 해설 : 29(12+17), 32(8+9+15), 34(11+23) 로 분배하면 최대금액과 최소금액의 차가 5가 되어 5가 최 소차가 된다.

import sys
import math

#sys.stdin=open("in1.txt", "r")

def f_check(v):
    global cnt
    if v == N:
        # 같은 수가 없는지 판별
        # tmp = set()
        # for k in b
        #  tmp.add(k)
        # if len(tmp) == 3
        if b[0] != b[1] and b[1] != b[2] and b[2] != b[0]:
            # 최대, 최솟값의 차가 cnt보다 작으면 그 값으로 변환
            if cnt > (max(b) - min(b)):
                cnt = (max(b) - min(b))
    else:
        if v < N:
            for j in range(0, 3):
                b[j] += a[v]
                f_check(v + 1)
                b[j] -= a[v]

N = int(input())
a = []
b = [0] * 3
for i in range(0, N):
    a.append(int(input()))
cnt = sum(a)
f_check(0)
print(cnt)
