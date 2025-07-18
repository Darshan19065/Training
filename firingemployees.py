a=["a","b","c","d","e","f","g","h","i","j"]
b=[0,1,1,1,2,2,1,2,1,2]
c=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
d=list(zip(a,b,c))
count=0
e=[]
for i in d:
    if(int(i[2])>4000):
        e.append(i)
        d.remove(i)
        count=count+1
        if count>1:
            break
e.sort(key=lambda x:x[2],reverse=True)
d.sort(key=lambda x:x[2],reverse=True)
for i in d:
    if (i[1])>=2 and count<5:
        e.append(i)
        d.remove(i)
        count=count+1
for i in e:
    print("name:",i[0],"memo:",i[1],"salary:",i[2])

