get=int(input())
l1=list(map(int,input().split()[:get]))
l1.sort()
for p in l1:
        print(p,end=" ")
