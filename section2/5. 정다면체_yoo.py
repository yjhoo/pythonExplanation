# print(c[j], end = ' ') - 출력되는 마지막 부분에 개행문자 대신에 공백을 넣어줌
# 정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요. 정답이 여러 개일 경우 오름차순으로 출력합니다.
# ▣ 입력설명 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# ▣ 출력설명 첫 번째 줄에 답을 출력합니다.
# ▣ 입력예제 1                                   4 6
# ▣ 출력예제 1 5 6 7

import sys
#sys.stdin=open("in1.txt", "rt")

N, M = map(int, input().split())
a = []
# 나올 수 있는 모든 경우의 수 구함
for i in range(1, N + 1):
    for j in range(1, M + 1):
        a.append(i + j)
# 경우의 수만큼 배열 생성
b = [0] * a[len(a) - 1]
# 배열에 나온 수 만큼 값 넣어줌
for j in range(0, len(a)):
    b[a[j] - 1] += 1
c = []
# max 값과 같은 값을 배열 c에 넣어줌
for i in range(0, len(b)):
    if max(b) == b[i]:
        c.append(i+1)
for j in range(0, len(c)):
    print(c[j], end = ' ')

