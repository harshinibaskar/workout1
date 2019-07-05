ka,la=map(int,input().split())
l=list(map(int,input().split()[:ka]))
count=0
for i in l:
   if(i==la):
      count=count+1
print(count)      
