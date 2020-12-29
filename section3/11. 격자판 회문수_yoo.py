# 격자판 회문수
# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
# 빨간색처럼 구부러진 경우(87178)는 회문수로 간주하지 않습니다.
# ▣ 입력설명 1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
# ▣ 출력설명 5자리 회문수의 개수를 출력합니다.
# ▣ 입력예제 1                                   2 4 1 5 3 2 6 3 5 1 8 7 1 7 8 3 2 7 1 3 8 6 1 2 3 2 1 1 1 3 1 3 5 3 2 1 1 2 5 6 5 2 1 2 2 2 2 1 5
# ▣ 출력예제 1 3

import sys
import math
#sys.stdin=open("in2.txt", "rt")

# 5자리의 회문수를 판별하는 함수 / 가로와 세로열을 함께 확인한다.
def check(arr, num):
    count = 0
    for j in range(0, 3):
        if arr[num][j] == arr[num][j + 4] and arr[num][j+1] == arr[num][j + 3]:
            count += 1
        if arr[j][num] == arr[j + 4][num] and arr[j+1][num] == arr[j + 3][num]:
            count += 1
    return count


arr = [[int(x) for x in input().split()]for y in range(7)]
answer = 0
for i in range(0, 7):
    answer += check(arr, i)
print(answer)
