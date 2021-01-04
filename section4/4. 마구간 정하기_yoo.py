# 마구간 정하기(결정알고리즘)
# N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마 구간간에 좌표가 중복되는 일은 없습니다. 현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다. C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.
# ▣ 입력설명 첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다. 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.
# ▣ 출력설명 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
# ▣ 입력예제 1                                   5 3 1 2 8 4 9
# ▣ 출력예제 1 3

import sys
import math
#sys.stdin=open("in1.txt", "rt")

#마굿간의 갯수를 구하는 함수
def check(m):
    count = 1
    tmp = arr[0]
    for j in range(1, N):
        # 이전 마굿간과의 거리가 입력된 m보다 클 경우 마굿간 갯수 +1, tmp에 현재 마굿간의 위치 입력해줌
        if arr[j] - tmp >= m:
            count += 1
            tmp = arr[j]
    return count


N, M = map(int, input().split())
arr = []
for i in range(0, N):
    arr.append(int(input()))
arr.sort()
lt = arr[0]
rt = arr[N - 1]
m = (rt + lt) // 2
while lt <= rt:
    # 마굿간의 갯수가 기준 값인 M보다 큰지 작은지를 판별
    if check(m) >= M:
        # 갯수가 클 경우 현재값 저장 후 최솟값을 m + 1로 세팅
        answer = m
        lt = m + 1
    else:
        # 갯수가 작을 경우 답이 될 수 없으므로 최댓값만 m -1로 세팅
        rt = m - 1
    m = (rt + lt) // 2

print(m)








