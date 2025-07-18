a="00000aaabbcccccaa"
c=0
res=""
for i in range(len(a)):
    if i+1<len(a)and a[i]==a[i+1]:
        c=c+1
    else:
        res=res+a[i]+str(c)
        c=1
print(res)