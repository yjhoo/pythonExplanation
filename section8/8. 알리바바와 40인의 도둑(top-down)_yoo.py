# 알리바바와 40인의 도둑(Top-Down)
# 알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다. 알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다. 계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 각 돌다리들은 높이가 서로 다릅니다. 해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다. 즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다. N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요. 만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면
# 3 3 5
# 2 3 4
# 6 5 2
# (1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.
# ▣ 입력설명 첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다. 두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.
# ▣ 출력설명 첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.
# ▣ 입력예제 1                                   5 3 7 2 1 9 5 8 3 9 2 5 3 1 2 3 5 4 3 2 1 1 7 5 2 4
# ▣ 출력예제 1 25

import sys

#sys.stdin = open('in5.txt', 'r')

def f_check(x, y):
    # d값이 0이 아닐 경우에 바로 return
    # 가장 윗줄일 경우 옆에 값으로 더하기
    # 가장 왼쪽줄인 경우 위에 값으로 더하기
    # 아닌 경우엔 x,y값 하나 전의 값중 작은 값으로 더하기
    if d[x][y] != 0:
        return d[x][y]
    elif x == 0 and y == 0:
        d[x][y] = l[x][y]
    elif x == 0:
        d[x][y] = l[x][y] + f_check(x, y-1)
    elif y == 0:
        d[x][y] = l[x][y] + f_check(x-1, y)
    else:
        d[x][y] = l[x][y] + min(f_check(x, y-1), f_check(x-1, y))
    return d[x][y]

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * N for _ in range(N)]
print(f_check(N-1, N-1))
