# Anagram(아나그램 : 구글 인터뷰 문제)
# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아 나그램이라고 합니다. 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재 배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다. 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세 요. 아나그램 판별시 대소문자가 구분됩니다.
# ▣ 입력설명 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다. 단어의 길이는 100을 넘지 않습니다.
# ▣ 출력설명 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
# ▣ 입력예제 1                                   AbaAeCe baeeACA
# ▣ 출력예제 1 YES

import sys
import math
from collections import deque

#sys.stdin = open("in4.txt", "rt")
p = dict()
A = list(input())
# A ~ z까지 0으로 초기화
for k in range(65, 123):
    p[chr(k)] = 0
# 문자마다 값 1씩 증가
for i in A:
    p[i] += 1
B = list(input())
# 문자마다 값 1씩 감소 , 감소할때 값이 -값이 나오면 NO print하고 종료 / 마지막까지가면 YES print
for j in B:
    if p[j] > 0:
        p[j] -= 1
    else:
        print("NO")
        sys.exit()
print("YES")
