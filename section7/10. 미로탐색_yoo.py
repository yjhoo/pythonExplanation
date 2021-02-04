# 미로탐색(DFS)
# 7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요.  출발점은 격 자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 통로이다. 격 자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
# 출발 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 도착
# 위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.
# ▣ 입력설명 7*7 격자판의 정보가 주어집니다.
# ▣ 출력설명 첫 번째 줄에 경로의 가지수를 출력한다.
# ▣ 입력예제 1                                   0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 0 0 0 1 1 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 1 1 0 0 1 0 0 0 0 0 0
# ▣ 출력예제 1 8

import sys
import math

#sys.stdin=open("in1.txt", "r")
# m_x - x 값, m_y - y값
def f_check(m_x, m_y):
    global cnt
    # 최종에 도달하면 cnt 추가
    if m_x == 6 and m_y == 6:
        cnt += 1
    # 상하좌우로 움직이되 갔던 곳은 다시 안가도록 1로 수정함
    if m_x < 6:
        if a[m_x+1][m_y] == 0:
            a[m_x+1][m_y] = 1
            f_check(m_x + 1, m_y)
            a[m_x + 1][m_y] = 0
    if m_y < 6:
        if a[m_x][m_y + 1] == 0:
            a[m_x][m_y + 1] = 1
            f_check(m_x, m_y + 1)
            a[m_x][m_y + 1] = 0
    if m_x > 1:
        if a[m_x-1][m_y] == 0:
            a[m_x - 1][m_y] = 1
            f_check(m_x - 1, m_y)
            a[m_x - 1][m_y] = 0
    if m_y > 1:
        if a[m_x][m_y - 1] == 0:
            a[m_x][m_y - 1] = 1
            f_check(m_x, m_y - 1)
            a[m_x][m_y - 1] = 0
a = [[int(x) for x in map(int, input().split())] for y in range(7)]
cnt = 0
f_check(0, 0)
print(cnt)
