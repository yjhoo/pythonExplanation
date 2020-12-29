# 자릿수의 합
# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
# ▣ 입력설명 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.
# ▣ 출력설명 자릿수의 합이 최대인 자연수를 출력한다.
# ▣ 입력예제 1                                   3 125 15232 97
# ▣ 출력예제 1 97

import sys
#sys.stdin=open("in2.txt", "rt")
# 자연수의 자리의 합을 구하는 함수
def digit_sum(x):
    a = 0
    while x > 0:
        a += x % 10
        x = x // 10
    return a

N = int(input())
a = list(map(int, input().split()))
m = 0
c = 0
for i in range(0, len(a) - 1):
    # 기존의 max 값보다 큰 값이 있으면 새로운 값으로 교체 / 해당 값의 위치를 알기 위해서 i 값도 저장
    if m < digit_sum(a[i]):
        m = digit_sum(a[i])
        c = i

print(a[c])

