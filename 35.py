mock=input()
test=0
for i in range(len(mock)):
  if(mock[i].isdigit()):
    test+=1
print(test)
