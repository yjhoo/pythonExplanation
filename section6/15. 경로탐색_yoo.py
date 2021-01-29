# 경로 탐색(그래프 DFS)
# 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프 로그램을 작성하세요. 아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지 수는
# 1 2 3 4 5 1 2 5 1 3 4 2 5 1 3 4 5 1 4 2 5 1 4 5
# 총 6 가지입니다.
# ▣ 입력설명 첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연 결정보가 주어진다.
# ▣ 출력설명 총 가지수를 출력한다.
# ▣ 입력예제 1                                   5 9 1 2 1 3 1 4 2 1 2 3 2 5 3 4 4 2 4 5
# ▣ 출력예제 1 6


import sys
#sys.stdin=open("in1.txt", "r")

def f_check(v):
    global cnt
    # N에 도달했을 경우 cnt 추가
    if v == N - 1:
        cnt += 1
    else:
        # 1에서 시작해야하므로 다음 번째 부터 판별하기 위해 range를 1부터 시작
        for j in range(1, N):
            if a[v][j] == 1 and c[j] == 0:
                c[j] = 1
                f_check(j)
                c[j] = 0

N, M =map(int, input().split())
a = [[0] * N for _ in range(N)]
for i in range(0, M):
    b = list(map(int, input().split()))
    # 이동할 수 있는 부분 입력
    a[b[0]-1][b[1]-1] = 1
c = [0] * N
cnt = 0
f_check(0)
print(cnt)
