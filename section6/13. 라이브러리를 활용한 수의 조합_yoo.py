import sys
import itertools as it
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
# combinations <- 조합을 만드는 함수
# itertools.combinations을 이용하여 조합을 만들고 합을 구해서 계산할 수 있도록 함
for x in it.combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)
