# 수들의 조합
# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수 는 몇 개가 있는지 출력하는 프로그램을 작성하세요. 예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지가 있습니다.
# ▣ 입력설명 첫줄에 정수의 개수 N(3<=N<=20)과 임의의 정수 K(2<=K<=N)가 주어지고, 두 번째 줄에는 N개의 정수가 주어진다. 세 번째 줄에 M이 주어집니다.
# ▣ 출력설명 총 가지수를 출력합니다.
# ▣ 입력예제 1                                   5 3 2 4 5 8 12 6
# ▣ 출력예제 1 2

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

# v = 입력되는 배열의 피봇, s = 추가된 배열의 수, t =  총합
def f_check(v, s, t):
    global cnt
    # s값이 K에 도달하면 배열의 숫자가 모두 채워진 것으로 보고 판별한다.
    if s == K:
        if t % M == 0:
            cnt += 1
    else:
        # 처음에 입력된 피봇수를 기준으로 N까지 for문 수행
        # i값을 기준으로 다음 값을 지정하고 그 i 값에 있는 a의 값을 총합에 추가하며 s를 1 증가시킨다.
        for i in range(v, N):
            f_check(i+1, s+1, t + a[i])

N, K = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())
l = [0] * N
cnt = 0
f_check(0, 0, 0)
print(cnt)
