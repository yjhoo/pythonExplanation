# 재귀함수를 이용한 이진수 출력
# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용 해서 출력해야 합니다.
# ▣ 입력설명 첫 번째 줄에 10진수 N(1<=N<=1,000)이 주어집니다.
# ▣ 출력설명 첫 번째 줄에 이진수를 출력하세요.
# ▣ 입력예제 1                                   11
# ▣ 출력예제 1 1011

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

# 이진수로 만들어주는 함수
def f_two(num):
    if num == 0:
        return
    else:
        # num이 0이 아니면 2로나는 몫을 다시 함수에 넣고 나머지는 print함
        f_two(num//2)
        print(num % 2, end='')

N = int(input())
f_two(N)

