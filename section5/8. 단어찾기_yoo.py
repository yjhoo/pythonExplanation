# 단어 찾기
# 현수는 영어로 시는 쓰는 것을 좋아합니다. 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다. 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 여러분이 찾아 주세요.
# ▣ 입력설명 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다. 두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.
# ▣ 출력설명 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
# ▣ 입력예제 1                                   5 big good sky blue mouse sky good mouse big
# ▣ 출력예제 1 blue


import sys
import math
from collections import deque

#sys.stdin = open("in2.txt", "rt")

N = int(input())
l = []
r = []
# l에 노트에 들어갈 값 / r에 시에 쓴 값을 넣어두고 마지막 for문에서 노트에 들어있는데 r에 없는 값을 출력하게 함
for i in range(0, N):
    l.append(str(input()))
for j in range(0, N-1):
    r.append(str(input()))
for x in l:
    if not any(x == y for y in r):
        print(x)
