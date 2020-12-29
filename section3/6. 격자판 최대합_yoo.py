# 5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.
# ▣ 입력설명 첫 줄에 자연수 N이 주어진다.(1<=N<=50) 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.
# ▣ 출력설명 최대합을 출력합니다.
# ▣ 입력예제 1                                   5 10 13 10 12 15 12 39 30 23 11 11 25 50 53 15 19 27 29 37 27 19 13 30 13 19
# ▣ 출력예제 1 155

import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = [[int(x) for x in input().split()]for y in range(N)]

m = 0
low = 0
col = 0
parr = [0] * N
marr = [0] * N
for i in range(0, N):
    low = 0
    col = 0
    for j in range(0, N):
        # 가로행의 합 계산
        low += arr[i][j]
        # 세로열의 합 계산
        col += arr[j][i]
        # 대각선의 합을 구함
        for k in range(0, N):
            if i - j == k:
                parr[k] += arr[i][j]
        for k in range(0, N):
            if j - i == k:
                marr[k] += arr[i][j]
    # 가로행의 합이 최대일 경우 m에 저장
    if m < low:
        m = low
    # 세로행의 합이 최대일 경우 m에 저장
    if m < col:
        m = col
# 대각선의 합을 구한 값중에서 가장 큰 값이 있으면 그 값으로 m 저장
for i in range(0, N):
    if parr[i] > m:
        m = parr[i]
    if marr[i] > m:
        m = marr[i]
print(m)
