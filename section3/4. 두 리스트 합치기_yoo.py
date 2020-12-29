# 두 리스트 합치기
# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
# ▣ 입력설명 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다. 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다. 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
# ▣ 출력설명 오름차순으로 정렬된 리스트를 출력합니다.
# ▣ 입력예제 1                                   3 1 3 5 5 2 3 6 7 9
# ▣ 출력예제 1 1 2 3 3 5 6 7 9

import sys
import math
#sys.stdin=open("in1.txt", "rt")

a = int(input())
arr1 = list(map(int, input().split()))
b = int(input())
arr2 = list(map(int, input().split()))
c = 0
d = 0
answer = []
for i in range(0, a+b):
    # arr1, arr2의 마지막에 도닿앴을 경우 둘중 남아 있는 것으로 채워줌
    if c == a:
        for j in range(d, b):
            answer.append(arr2[j])
        break
    elif d == b:
        for j in range(c, a):
            answer.append(arr1[j])
        break
    # 값이 작은 쪽으로 answer 배열 채워줌
    if arr1[c] <= arr2[d]:
        answer.append(arr1[c])
        c += 1
    else:
        answer.append(arr2[d])
        d += 1
for i in range(0, len(answer)):
    print(answer[i], end=' ')
