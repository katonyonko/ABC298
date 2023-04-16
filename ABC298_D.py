import io
import sys

_INPUT = """\
6
3
3
1 2
3
3
1 5
2
3
11
1 9
1 9
1 8
1 2
1 4
1 4
1 3
1 5
1 3
2
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  mod=998244353
  Q=int(input())
  h=deque([1])
  S=1
  for _ in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
      x=query[1]
      h.append(x)
      S*=10
      S+=x
      S%=mod
    elif query[0]==2:
      x=h.popleft()
      S-=x*pow(10,len(h),mod)
      S%=mod
    else: print(S)