g=int(input())
n1,n2=0,1
print(n2,end=" ")
for i in range(1,g):
  r=n1+n2
  print(r,end=" ")
  n1,n2=n2,r
