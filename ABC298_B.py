import io
import sys

_INPUT = """\
6
3
0 1 1
1 0 0
0 1 0
1 1 0
0 0 1
1 1 1
2
0 0
0 0
1 1
1 1
5
0 0 1 1 0
1 0 0 1 0
0 0 1 0 1
0 1 0 1 0
0 1 0 0 1
1 1 0 0 1
0 1 1 1 0
0 0 1 1 1
1 0 1 0 1
1 1 0 1 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[list(map(int,input().split())) for _ in range(N)]
  B=[list(map(int,input().split())) for _ in range(N)]
  ans='No'
  def judge(X,Y):
    global ans
    flg=0
    for i in range(N):
      for j in range(N):
        if X[i][j]==1 and Y[i][j]==0: flg=1
    if flg==0: ans='Yes'
  for i in range(4):
    judge(A,B)
    A=[[A[N-1-j][i] for j in range(N)] for i in range(N)]
  print(ans)