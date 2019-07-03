l=int(input())
if l>1:
 for i in range(2,s):
    if l%i==0:
        print("no")
        break
  else:
        print("yes")
else:
        print("no")
