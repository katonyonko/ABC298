import io
import sys

_INPUT = """\
6
4
1 1 2
1 2 9
2 1 8
3 2 3
1
1 1000000000 1
15
158260522 877914575 602436426
24979445 861648772 623690081
433933447 476190629 262703497
211047202 971407775 628894325
731963982 822804784 450968417
430302156 982631932 161735902
880895728 923078537 707723857
189330739 910286918 802329211
404539679 303238506 317063340
492686568 773361868 125660016
650287940 839296263 462224593
492601449 384836991 191890310
576823355 782177068 404011431
818008580 954291757 160449218
155374934 840594328 164163676
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  R=defaultdict(int)
  C=defaultdict(int)
  d=dict()
  # s=defaultdict(set)
  for _ in range(N):
    r,c,x=map(int,input().split())
    R[r]+=x
    C[c]+=x
    d[(r,c)]=x
    # s[r].add(c)
  # R2=sorted([(R[k],k) for k in R], key=lambda x: -x[0])
  C2=sorted([(C[k],k) for k in C], key=lambda x: -x[0])
  ans=0
  for r in R:
    now=0
    tmp=R[r]+C2[now][0]
    if (r,C2[now][1]) in d: tmp-=d[(r,C2[now][1])]
    ans=max(ans,tmp)
    while (r,C2[now][1]) in d:
      now+=1
      if now==len(C2): break
      tmp=R[r]+C2[now][0]
      if (r,C2[now][1]) in d: tmp-=d[(r,C2[now][1])]
      ans=max(ans,tmp)
      if tmp==21: print(r,now)
  print(ans)