# 최대점수 구하기(냅색 알고리즘)
# 이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 합니다. 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩 니다. 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. (해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)
# ▣ 입력설명 첫 번째 줄에 문제의 개수N(1<=N<=100)과 제한 시간 M(10<=M<=1000)이 주어집니다. 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
# ▣ 출력설명 첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.
# ▣ 입력예제 1                                   5 20 10 5 25 12 15 8 6 3 7 4
# ▣ 출력예제 1 41

import sys

#sys.stdin = open('in1.txt', 'r')

N, M = map(int, input().split())
c = [0] * (M+1)
for _ in range(N):
    a, b = map(int, input().split())
    # 입력되는 점수에 대해서 이전의 점수와 비교하여 비교 값이 클 경우 저장
    for i in range(M, b-1, -1):
        c[i] = max(c[i], c[i-b] + a)
print(c[M])
