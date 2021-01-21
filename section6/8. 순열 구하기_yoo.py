# 순열 구하기
# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중  M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
# ▣ 입력설명 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# ▣ 출력설명 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.
# ▣ 입력예제 1                                   3 2
# ▣ 출력예제 1 1 2 1 3 2 1 2 3 3 1 3 2 6

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_row(v):
    global cnt
    # N개 만큼 0이 있는 배열에서 0인 부분을 1로 바꾸고 그 값을 a배열에 넣어줌
    # v의 값이 M - 1 만큼 되면 a안에 있는 값을 print하고 cnt 증가
    # for문 마지막에서 l[i]값을 다시 0으로 바꾸고 a의 배열에서도 값 제거
    for i in range(0, N):
        if l[i] == 0:
            l[i] = 1
            a.append(i+1)
            if v == M - 1:
                for j in a:
                    print(j, end=' ')
                print()
                cnt += 1
            else:
                f_row(v+1)
            l[i] = 0
            a.remove(i+1)
N, M = map(int, input().split())
l = [0] * N
a = []
cnt = 0
f_row(0)
print(cnt)
