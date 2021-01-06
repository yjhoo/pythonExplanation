# 가장 큰 수
# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다) 만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.
# ▣ 입력설명 첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
# ▣ 출력설명 가장 큰 수를 출력합니다.
# ▣ 입력예제 1                                   5276823 3
# ▣ 출력예제 1 7823
# ▣ 입력예제 2                                   9977252641 5
# ▣ 출력예제 2 99776

import sys
import math
#sys.stdin=open("in1.txt", "rt")

N, m = map(int, input().split())
# 숫자로 받은 값을 list에 저장
N = list(map(int, str(N)))
stack = []
for x in N:
    # stack에 값이 있고, m > 0인 상태에서 마지막으로 들어온 숫자가 현재 값보다 작을 경우 마지막 값 outgkrh m -1해줌
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    # stack에 값 추가
    stack.append(x)
# N의 모든 자릿수에 대한 과정을 거쳤음에도 m의 값이 0보다 크면 stack에 m의 자릿수만큼 뒷부분 제거
if m != 0:
    stack = stack[:-m]
# stack을 다시 하나의 숫자로 합쳐줌
res = ''.join(map(str, stack))
print(res)
