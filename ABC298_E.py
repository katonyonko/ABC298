import io
import sys

_INPUT = """\
6
4 2 3 3 2
6 4 2 1 1
100 1 1 10 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,A,B,P,Q=map(int,input().split())
  p=pow(P,mod-2,mod)
  q=pow(Q,mod-2,mod)
  dp=[0]*(2*100**2)
  def idx(i,j,k):return i*200+j*2+k
  for i in range(100):
    for j in range(100):
      for k in range(2):
        if k==0:
          if i==0: dp[idx(i,j,k)]=1
          else:
            if j==0: dp[idx(i,j,k)]=0
            else:
              for l in range(P):
                dp[idx(i,j,k)]+=dp[idx(max(i-l-1,0),j,1)]*p
              dp[idx(i,j,k)]%=mod
        else:
          if i==0: dp[idx(i,j,k)]=1
          else:
            if j==0: dp[idx(i,j,k)]=0
            else:
              for l in range(Q):
                dp[idx(i,j,k)]+=dp[idx(i,max(j-l-1,0),0)]*q
              dp[idx(i,j,k)]%=mod
  print(dp[idx(N-A,N-B,0)])