# 플로이드 워샬 알고리즘
# N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 때 모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값을 구하는 프로그램을 작성하 세요.
# 6 1 2 5 13
# 2 33
# 7
# 3 4 5
# 1
# ▣ 입력설명 첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보 와 비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이 면 “1 2 13”으로 주어진다.
# ▣ 출력설명 모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력한다. 자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으 로 출력합니다.
# ▣ 입력예제 1                                   5 8 1 2 6 1 3 3 3 2 2 2 4 1 2 5 13 3 4 5 4 2 3 4 5 7
# ▣ 출력예제 1 0 5 3 6 13 //1번 정점에서 2번정점으로 5, 1에서 3번 정점으로 3, 1에서 4번 정점으로 6...... M 0 M 1 8  //2번 정점에서 1번 정점으로는 갈수 없으므로 “M", ....... M 2 0 3 10 M 3 M 0 7 M M M M 0

import sys
from collections import deque

#sys.stdin = open('in1.txt', 'r')

N, M = map(int, input().split())
# 이차원 배열 초기화
l = [[400000]*N for _ in range(N)]
# 입력되는 초기값으로 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    if l[a-1][b-1] > c:
        l[a-1][b-1] = c
q = deque()
for i in range(N):
    for j in range(N):
        # 모든 배열에 있는 값을 1번은 큐에 추가
        q.append((i, j, l[i][j]))
        while(q):
            tmp = q.popleft()
            a = tmp[0]
            b = tmp[1]
            c = tmp[2]
            for k in range(N):
                # 큐에서 가져온 값보다 새롭게 만들어지는 값이 더 작을 경우에 그 시행도 큐에 추가하여 다시 넣고 작업 수행
                if l[k][b] > l[k][a] + c:
                    l[k][b] = l[k][a] + c
                    q.append((k, b, l[k][b]))

# i == j 면 0
# 값이 변화된 적이 없으면 M
# 아니면 그 값을 출력하도록 함
for i in range(N):
    for j in range(N):
        if i == j:
            print(0, end=' ')
        elif l[i][j] == 400000:
            print('M', end = ' ')
        else:
            print(l[i][j], end =' ')
    print()
