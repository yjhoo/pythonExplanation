# 바둑이 승차(DFS)
# 철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태
# 울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운
# 무게를 구하는 프로그램을 작성하세요.
# ▣ 입력설명 첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 둘째 줄부터 N마리 바둑이의 무게가 주어진다.
# ▣ 출력설명 첫 번째 줄에 가장 무거운 무게를 출력한다.
# ▣ 입력예제 1                                   259 5
# 81
# 58
# 42
# 33
# 61
# ▣ 출력예제 1 242

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

# v - 피봇, s - 합, m - 최대값
# m보다 s가 크면 m에 s대입
# m == C이면 종료
# m < C / v != N-1에서 다음 값의 합이 C보다 같거나 작을 경우 더하고, 아니면 안더하고 다음으로 진행
def f_DFS(v, s, m):
    if s > m:
        m = s
    if m == C:
        print(C)
        sys.exit()
    if m < C:
        if v != N-1:
            if C >= s + l[v+1]:
                f_DFS(v + 1, s + l[v + 1], m)
            f_DFS(v+1, s, m)
    a.append(m)

C,N = map(int,input().split())
l = []
a = []
M = 0
# 숫자 배열에 넣어줌 / 벼열에 넣은 총 합이 C 보다 적으면 합을 print하고 종료
for i in range(0, N):
    l.append(int(input()))
    M += l[i]
if M < C:
    print(M)
    sys.exit()
f_DFS(-1, 0, 0)
print(max(a))
