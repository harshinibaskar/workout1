m=int(input())
a=list(map(int,input().split()[:m]))
a.sort()
for v in a:
  print(v,end=" ")
