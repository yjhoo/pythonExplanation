import sys
import itertools as it
sys.stdin=open("input.txt", "rt")
n, f=map(int, input().split())
b=[1]*n
cnt=0
# b행렬에 이항계수 구해서 입력함
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))
# permutations <- 수열을 만들어주는 함수
# itertools.permutations를 이용해서 배열 a의 수열을 만듦
# 만들어진 수열에 대해서 b의 이항계수값을 서로 곱하여 값을 구하고 이를 sum에 추가함
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break
