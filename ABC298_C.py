import io
import sys

_INPUT = """\
6
5
8
1 1 1
1 2 4
1 1 4
2 4
1 1 4
2 4
3 1
3 2
1
5
1 1 1
1 2 1
1 200000 1
2 1
3 200000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  N=int(input())
  Q=int(input())
  q2=[[] for _ in range(N)]
  q3=[[] for _ in range(2*10**5)]
  q3t=[set() for _ in range(2*10**5)]
  for _ in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
      i,j=query[1:]
      heappush(q2[j-1],i-1)
      if j-1 not in q3t[i-1]:
        q3t[i-1].add(j-1)
        heappush(q3[i-1],j-1)
    elif query[0]==2:
      i=query[1]
      tmp=[]
      while q2[i-1]:
        x=heappop(q2[i-1])
        tmp.append(x)
      print(*[tmp[j]+1 for j in range(len(tmp))])
      for j in range(len(tmp)):
        heappush(q2[i-1],tmp[j])
    else:
      i=query[1]
      tmp=[]
      while q3[i-1]:
        x=heappop(q3[i-1])
        tmp.append(x)
      print(*[tmp[j]+1 for j in range(len(tmp))])
      for j in range(len(tmp)):
        heappush(q3[i-1],tmp[j])