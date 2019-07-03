a,b=map(int,input().split())
for k in range(a+1,b,1):
    if(k>1):
       for j in range(2,k)
          if(k%j==0):
              break
     else:
          print(k,end=" ")
       
