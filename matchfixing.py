team=[]
a=int(input("enter the number of teams"))
for i in range(a):
    team.append(input("enter the name"))
b=int(input("enter the number of meetd"))
matches=[]
for i in range(b):
    for j in (team):
        matches.append([team[j],team[j+1]])
print(matches)