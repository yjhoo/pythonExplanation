# 스토쿠 검사
# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
#   위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오 고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다. 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.
# ▣ 입력설명 첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
# ▣ 출력설명 첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

import sys
import math
#sys.stdin=open("in2.txt", "rt")

arr = [[int(x) for x in input().split()]for y in range(9)]
# 가로 9 줄, 세로 9 줄, 3x3정사각형 9개
arr1 = [[False for x in range(9)] for y in range(27)]
c, d = 0, 0
for i in range(0, 9):
    for j in range(0, 9):
        c, d = 0, 0
        # 처음나오는 숫자면 True로 입력하고 이미 나온적이 있는 값일 경우 NO 출력 후 시스템 종료
        if not arr1[i][arr[i][j]-1]:
            arr1[i][arr[i][j]-1] = True
        else:
            print('NO')
            sys.exit()
        if not arr1[i+9][arr[j][i]-1]:
            arr1[i+9][arr[j][i]-1] = True
        else:
            print('NO')
            sys.exit()
        c = i // 3
        d = (j // 3) * 3
        if not arr1[18 + c + d][arr[i][j]-1]:
            arr1[18 + c + d][arr[i][j]-1] = True
        else:
            print('NO')
            sys.exit()
# 마지막까지 도달했을 경우 YES 출력
print('YES')
