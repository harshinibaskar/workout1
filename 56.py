post=input()
for i in range(0,len(post)):
   if(post[i].isalpha() and post[i].isdigit()):
    print("No")
else:
  print("Yes")
