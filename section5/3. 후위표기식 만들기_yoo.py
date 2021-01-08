# 후위표기식 만들기
# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요. 중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있 으면 중위표기식입니다. 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다. 예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다. 만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면 (3+5)*2 이면 35+2* 로 바꾸어야 합니다.
# ※후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.
# ▣ 입력설명 첫 줄에 중위표기식이 주어진다.  길이는 100을 넘지 않는다. 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
# ▣ 출력설명 후위표기식을 출력한다.
# ▣ 입력예제 1                                   3+5*2/(7-2)
# ▣ 출력예제 1 352*72-/+
# ▣ 입력예제 2                                   3*(5+2)-9
# ▣ 출력예제 2 352+*9

import sys
import math

#sys.stdin = open("in4.txt", "rt")

# 후위표기식을 만들기 위한 함수
def Hu(arr):
    tmp = []
    i = 0
    check = 0
    # 후위표기식이 만들어질때 까지 반복 수행
    while len(arr) > 1:
        # 괄호를 우선순위 1순위로 표현
        # 괄호 값을 계산하고 그 새로운 결과 값을 붙여서 Hu() 다시 수행
        if arr[i] == '(':
            c = 1
            while arr[i + c] != ')':
                tmp.append(arr[i + c])
                c += 1
            tmp1 = arr[:i]
            tmp2 = Hu(tmp)
            tmp1.append(tmp2)
            arr = tmp1 + arr[i + c + 1:]
            arr[0] = Hu(arr)
            break
        # *, /를 우선순위 2순위로 표현
        # 값을 계산하고 그 새로운 결과 값을 붙여서 Hu() 다시 수행
        if (arr[i] == '*' or arr[i] == '/') and check == 1:
            tmp = arr[i - 1] + arr[i + 1] + arr[i]
            tmp1 = arr[:i - 1]
            tmp1.append(tmp)
            arr = tmp1 + arr[i + 2:]
            arr[0] = Hu(arr)
            break
        # +, -를 우선순위 3순위로 표현
        # 값을 계산하고 그 새로운 결과 값을 붙여서 Hu() 다시 수행
        if (arr[i] == '+' or arr[i] == '-') and check == 2:
            tmp = arr[i - 1] + arr[i + 1] + arr[i]
            tmp1 = arr[:i - 1]
            tmp1.append(tmp)
            arr = tmp1 + arr[i + 2:]
            arr[0] = Hu(arr)
            break
        i += 1
        # 모든 값을 탐색해도 수행할 계산이 없을 경우 다음 순위로 넘어감
        if i == len(arr):
            i = 0
            check += 1
    return arr[0]

N = str(input())
N = list(map(str, N))
answer = Hu(N)
print(answer)

# 정답
# import sys
# sys.stdin=open("input.txt", "r")
# a=input()
# stack=[]
# res=''
# for x in a:
      # 숫자일 경우 res값에 추가
      # 숫자인지 판별하는 함수
#     if x.isdecimal():
#         res+=x
#     else:
          # '('면 스택에 저장
          # '*','/'면 바로 전의 값이 '*','/'일 경우 바로 전 값을 res에 저장 후 현재 값은 스택에 저장
          # '+','-'면 바로 전의 값이 '('일 경우를 제외하고 res 값에 저장 후 현재 값은 스택에 저장
          # ')'면 '('가 나올때까지 스택에 있는 값 모두 res에 저장하고 '('는 제거
#         if x=='(':
#             stack.append(x)
#         elif x=='*' or x=='/':
#             while stack and (stack[-1]=='*' or stack[-1]=='/'):
#                 res+=stack.pop()
#             stack.append(x)
#         elif x=='+' or x=='-':
#             while stack and stack[-1]!='(':
#                 res+=stack.pop()
#             stack.append(x)
#         elif x==')':
#             while stack and stack[-1]!='(':
#                 res+=stack.pop()
#             stack.pop()
# 모든 루프 돌고서 스택에 남아있는 값 res에 추가
# while stack:
#     res+=stack.pop()
# print(res)
