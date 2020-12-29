# 이분검색
# 임의의 N개의 숫자가 입력으로 주어집니다.  N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.
# ▣ 입력설명 첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
# ▣ 출력설명 첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.
# ▣ 입력예제 1                                   8 32 23 87 65 12 57 32 99 81
# ▣ 출력예제 1 3

import sys
import math
#sys.stdin=open("in1.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

min_num = 1
max_num = N-1
answer = 0
# 최소값이 최댓값보다 같거나 커질 때까지 반복
while min_num <= max_num:
    # 중간 값을 m에 저장
    m = (min_num + max_num) // 2
    # 목표 값이 중간값 보다 클 경우 min_num에 m + 1 값을 넣음
    if arr[m] < M:
        min_num = m + 1
    # 목표 값이 중간값 보다 작을 경우 max_num에 m - 1 값을 넣음
    elif arr[m] > M:
        max_num = m - 1
    # 값이 동일 할 경우 m + 1 값을 answer에 넣어줌 (0부터 시작이니까)
    if arr[m] == M:
        answer = m + 1
        print(answer)
        break


