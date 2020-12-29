# map(int, input().split()) - 공백으로 되어 있는 input 받아서 줌
# range(i,j) - i부터 j-1까지의 범위 읽음

import sys
p, q = map(int, input().split())
a = []
for x in range(1, p + 1):
    # 약수면 a list에 담아줌
    if p % x == 0:
        a.append(x)
# k번째가 a리스트의 길이 보다 작으면 값 보여주고 아니면 -1보여줌
if len(a) >= q:
    print(a[q-1])
else:
    print(-1)
