# 후위식 연산
# 후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요. 만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
# ▣ 입력설명 첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다. 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
# ▣ 출력설명 연산한 결과를 출력합니다.
# ▣ 입력예제 1                                   352+*9
# ▣ 출력예제 1 12

import sys
import math

#sys.stdin = open("in1.txt", "rt")

N = str(input())
N = list(map(str, N))
stack = []
tmp1 = 0
tmp2 = 0
tmp = 0
for i in N:
    # 숫자인지 판별 후 숫자이면 stack에 추가
    if i.isdecimal():
        stack.append(i)
    # 숫자가 아닐 경우 기호이므로 연산을 수행한다.
    # 모든 연산이 수행될 경우 남는 것은 숫자 하나 뿐이므로 그 값을 출력한다.
    else:
        tmp2 = int(stack.pop())
        tmp1 = int(stack.pop())
        if i == '+':
            tmp = tmp1 + tmp2
        elif i == '-':
            tmp = tmp1 - tmp2
        elif i == '*':
            tmp = tmp1 * tmp2
        else:
            tmp = tmp1 / tmp2
        stack.append(tmp)
print(stack.pop())
