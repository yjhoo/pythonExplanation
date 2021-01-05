# 증가수열 만들기(그리디)
# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다. 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열 을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니 다. 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다. 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 왼쪽 끝에서 5를 가져와  2 3 4 5 증가수열을 만들 수 있습니다.
# ▣ 입력설명 첫째 줄에 자연수 N(3<=N<=100)이 주어집니다. 두 번째 줄에 N개로 구성된 수열이 주어집니다.
# ▣ 출력설명 첫째 줄에 최대 증가수열의 길이를 출력합니다. 두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써 간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)
# ▣ 입력예제 1                                   5 2 4 5 1 3
# ▣ 출력예제 1 4 LRLL
# ▣ 입력예제 2                                   10 3 2 10 1 5 4 7 8 9 6
# ▣ 출력예제 2 3 LRR

import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
answer = ""
last = 0
while arr:
    # 양 끝수 모두 이전 숫자보다 크면 작은 숫자로 이전 수 변경
    if arr[0] > last and arr[len(arr) - 1] > last:
        if arr[0] < arr[len(arr) - 1]:
            last = arr[0]
            arr.remove(arr[0])
            answer += 'L'
        else:
            last = arr[len(arr) - 1]
            arr.remove(arr[len(arr) - 1])
            answer += 'R'
    # 왼쪽만 이전 숫자보다 크면 왼쪽 수로 이전 수 변경
    elif arr[0] > last:
        last = arr[0]
        arr.remove(arr[0])
        answer += 'L'
    # 오른쪽만 이전 숫자보다 크면 오른쪽 수로 이전 수 변경
    elif arr[len(arr) - 1] > last:
        last = arr[len(arr) - 1]
        arr.remove(arr[len(arr) - 1])
        answer += 'R'
    # 둘다 작으면 종료
    else:
        break
    # 종료 안됐을 경우 cnt +1
    cnt += 1
print(cnt)
print(answer)
