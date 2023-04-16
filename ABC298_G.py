import io
import sys

_INPUT = """\
6
2 3 4
2 3 4
4 1 3
2 2 3
0 0
0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W,T=map(int,input().split())
  s=[list(map(int,input().split())) for _ in range(H)]
  