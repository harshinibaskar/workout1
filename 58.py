go,dak=map(int,input().split())
l=list(map(int,input().split()[:go]))
count=0
for i in l:
   if(i==dak):
      print("yes")
      break
else:
   print("no")
