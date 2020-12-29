# 수들의 합
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# ▣ 입력설명 첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
# ▣ 출력설명 첫째 줄에 경우의 수를 출력한다.
# ▣ 입력예제 1                                   8 3 1 2 1 3 1 1 1 2
# ▣ 출력예제 1 5

import sys
import math
#sys.stdin=open("in5.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
tmp = 0
s = sum(arr)
for i in range(0, N):
    tmp = 0
    for j in range(i, N):
        # 추가되는 값이 M값을 초과하면 break
        if arr[j] > M:
            break
        tmp += arr[j]
        # 더한 값이 M값을 초과하면 break
        if tmp > M:
            break
        # 더한 값이 M과 같으면 answer 추가
        if tmp == M:
            answer += 1
            break
    # 남아있는 값이 M 보다 작으면 break
    s -= arr[i]
    if s < M:
        break
print(answer)
