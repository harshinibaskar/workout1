cm=input()
d=0
for i in range(len(cm)):
  if(cm[i].isdigit() or cm[i].isalpha() or cm[i]==(" ")):
    continue
  else:
    d+=1
print(d)
