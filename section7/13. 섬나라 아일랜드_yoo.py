# 섬나라 아일랜드(BFS 활용)
# 섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대 각선으로 연결되어 있으며, 0은 바다입니다. 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
# 만약 위와 같다면
# ▣ 입력설명 첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다. 두 번째 줄부터 격자판 정보가 주어진다.
# ▣ 출력설명 첫 번째 줄에 섬의 개수를 출력한다.
# ▣ 입력예제 1                                   7 1 1 0 0 0 1 0 0 1 1 0 1 1 0 0 1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 0 1 1 0 0 1 0 0 0 1 0 0 1 0 1 0 1 0 0
# ▣ 출력예제 1 5

import sys
import math
from collections import deque
#sys.stdin=open("in1.txt", "r")
# 상하좌우 대각선으로 움직이기 위한 피봇
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
# Queue 선언
q = deque()
for i in range(N):
    for j in range(N):
        if a[i][j] == 1:
            a[i][j] = 0
            # Queue에 추가
            q.append((i, j))
            cnt += 1
            # Queue가 존재할때 까지
            while q:
                tmp = q.popleft()
                # 상하좌우 대각선 모두 체크 후 진행 가능 하면 다음값 추가
                for k in range(8):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0 <= xx < N and 0 <= yy < N and a[xx][yy] == 1:
                        a[xx][yy] = 0
                        q.append((xx, yy))
print(cnt)
