grid=[]
for i in range(5):
    a=[]
    a.append(input("enter the name"))
    a.append(int(input("wntwe the marks 1")) )
    a.append(int(input("wntwe the marks 2")) )
    a.append(int(input("wntwe the marks 3")) )
    grid.append(a)
for i in range(5):
    sum=0
    for j in range(1,4):
        sum=sum+grid[i][j]
    print(i+1,".",grid[i][0],end=" ")
    print(sum/3)
            
            
        
