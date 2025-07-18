a=input("enter name 1")
b=input("enter name 2")
count=0
for i in a:
    if i in b:
        count=count-1
    else:
        count=count+1
count=count+len(b)
ans=["f","l","a","m","e"]
index=0
while(len(ans)!=1):
    index=(index+(count-1)%len(ans))
    ans.pop(index)
print(ans)