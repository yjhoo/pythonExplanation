# 사다리 타기(DFS)
# 현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 사다리 표현은 2차원 평면은 0으 로 채워지고, 사다리는 1로 표현합니다. 현수는 특정도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다. 여러분이 도와주세 요. 사다리의 지도가 10*10이면
# 0 1 2 3 4 5 6 7 8 9
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1
# 특정목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 됩니다.
# ▣ 입력설명 10*10의 사다리 지도가 주어집니다.
# ▣ 출력설명 출발지 열 번호를 출력하세요.
#
# ▣ 입력예제 1                                   1 0 1 0 0 1 0 1 0 1 1 0 1 1 1 1 0 1 0 1 1 0 1 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 1 1 0 1 0 0 1 0 1 0 1 1 0 1 1 1 1 0 1 0 1 1 0 1 0 0 1 0 1 1 1 1 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 1 1 0 1 1 0 1 0 0 2 0 1 0 1
# ▣ 출력예제 1 7


import sys

#sys.stdin = open("in1.txt", "r")

def f_check(m_x, m_y):
    # 지나갔다고 표시
    b[m_x][m_y] = 1
    # 시작지점에 도착하면 y값 출력
    if m_x == 0:
        print(m_y)
        sys.exit()
    else:
        # 지나갔는지 여부 및 이동가능 여부 확인하고 좌, 우, 위로 진행
        if m_y - 1 >= 0 and a[m_x][m_y - 1] == 1 and b[m_x][m_y - 1] == 0:
            f_check(m_x, m_y - 1)
        if m_y + 1 < 10 and a[m_x][m_y + 1] == 1 and b[m_x][m_y + 1] == 0:
            f_check(m_x, m_y + 1)
        else:
            f_check(m_x - 1, m_y)
# 값을 담은 2차원 배열
a = [list(map(int, input().split())) for _ in range(10)]
# 지나갔는지 여부를 확인하기 위한 2차원 배열
b = [[0]*10 for _ in range(10)]
for y in range(10):
    # 정답지점부터 출발
    if a[9][y] == 2:
        f_check(9, y)
