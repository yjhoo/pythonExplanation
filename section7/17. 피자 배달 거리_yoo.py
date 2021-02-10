import sys
import math
from collections import deque

#sys.stdin = open("in1.txt", "r")
def f_check(L, S):
    global cnt
    if L == M:
        total = 0
        for i in range(len(h)):
            tmp = 10000000
            for j in range(len(p)):
                for l in b:
                    if j == l and (abs(h[i][0] - p[j][0]) + abs(h[i][1] - p[j][1])) < tmp:
                        tmp = abs(h[i][0] - p[j][0]) + abs(h[i][1] - p[j][1])
            total += tmp
        if cnt > total:
            cnt = total
    else:
        for k in range(S, len(p)):
            b[L] = k
            f_check(L + 1, k + 1)

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
h = []
p = []
b = [0] * M
cnt = 1000000000
for x in range(N):
    for y in range(N):
        if a[x][y] == 1:
            h.append((x, y))
        if a[x][y] == 2:
            p.append((x, y))
f_check(0, 0)
print(cnt)
