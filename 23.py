a,b=map(int,input().split())
for f in range(a+1,b)
    ch=f
    find=0
 while(f>0):
    v=f%10
    find=find+(v**3)
    f=f//10
    if(find==ch):
      print(find,end" ")
