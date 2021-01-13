
import sys
import math

#sys.stdin = open("in1.txt", "rt")

N, K = map(int, input().split())
l = []
j = 0
cnt = 0
for i in range(1, N + 1):
    l.append(i)

while len(l) > 1:
    if j == len(l):
        j = 0
    cnt += 1
    if cnt % K == 0:
        l.remove(l[j])
    else:
        j += 1
print(l[0])
