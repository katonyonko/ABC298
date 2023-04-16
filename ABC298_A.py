import io
import sys

_INPUT = """\
6
4
oo--
3
---
1
o
100
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  if S.count('o')>0 and S.count('x')==0: print('Yes')
  else: print('No')