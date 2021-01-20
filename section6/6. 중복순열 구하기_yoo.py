# 중복순열 구하기
# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.
# ▣ 입력설명 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# ▣ 출력설명 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.
# ▣ 입력예제 1                                   3 2
# ▣ 출력예제 1 1 1 1 2 1 3 2 1 2 2 2 3 3 1 3 2 3 3 9

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")
def f_duplication(m):
    # cnt 변수를 글로벌 변수로 선언
    global cnt
    # 1~N까지 숫자 증가하도록 하고 그 값을 해당하는 배열 l에 넣어줌 /  길이가 M값에 도달하면 l값 출력
    for i in range(1, N + 1):
        l[M - m] = i
        if m == 1:
            for j in l:
                print(j, end=' ')
            cnt += 1
            print()
        if m > 1:
            f_duplication(m-1)

N, M = map(int, input().split())
l = [0] * M
cnt = 0
f_duplication(M)
print(cnt)

